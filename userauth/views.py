from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Profile, Story, LikeStory, Followers
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    try:
        if request.method == 'POST':
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            print(fnm, emailid, pwd)
            my_user = User.objects.create_user(fnm, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fnm)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request, my_user)
                return redirect('/')
            return redirect('/login')
    except:
        invalid = "User already exists"
        return render(request, 'signup.html', {'invalid': invalid})

    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/')
        invalid = "Invalid Credentials"
        return render(request, 'loginn.html', {'invalid': invalid})

    return render(request, 'loginn.html')

@login_required(login_url='/login')
def logouttt(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def home(request):
    following_users = Followers.objects.filter(follower=request.user.username).values_list('user', flat=True)
    story = Story.objects.filter(Q(user=request.user.username) | Q(user__in=following_users)).order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    context = {
        'story': story,
        'Profile': profile,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        caption = request.POST['caption']
        challenge = request.POST.get('challenge')
        short_description = request.POST.get('short_description')
        full_description = request.POST.get('full_description')
        category = request.POST.get('category')
        location = request.POST.get('location')
        google_map_link = request.POST.get('google_map_link')
        new_story = Story.objects.create(user=user, image=image, caption=caption, challenge=challenge,
                                         short_description=short_description, full_description=full_description,
                                         category=category, location=location, google_map_link=google_map_link)
        new_story.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/login')
def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        story = get_object_or_404(Story, id=id)
        like_filter = LikeStory.objects.filter(post_id=id, username=username).first()
        if like_filter is None:
            new_like = LikeStory.objects.create(post_id=id, username=username)
            story.no_of_likes = story.no_of_likes + 1
        else:
            like_filter.delete()
            story.no_of_likes = story.no_of_likes - 1
        story.save()
    return redirect('/')

@login_required(login_url='/login')
def home_story(request, id):
    story = Story.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'story': story,
        'profile': profile,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def explore(request):
    stories = Story.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    context = {
        'stories': stories,
        'profile': profile,
    }
    return render(request, 'explore.html', context)

@login_required(login_url='/login')
def profile(request, id_user):
    user_object = User.objects.get(username=id_user)
    profile = Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_stories = Story.objects.filter(user=id_user).order_by('-created_at')
    user_stories_length = len(user_stories)
    follower = request.user.username
    user = id_user

    if Followers.objects.filter(follower=follower, user=user).first():
        follow_unfollow = 'Unfollow'
    else:
        follow_unfollow = 'Follow'

    user_followers = len(Followers.objects.filter(user=id_user))
    user_following = len(Followers.objects.filter(follower=id_user))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_stories': user_stories,
        'user_stories_length': user_stories_length,
        'profile': profile,
        'follow_unfollow': follow_unfollow,
        'user_followers': user_followers,
        'user_following': user_following,
    }

    if request.user.username == id_user:
        if request.method == 'POST':
            if request.FILES.get('image') is None:
                image = user_profile.profileimg
                bio = request.POST['bio']
                location = request.POST['location']
                user_profile.profileimg = image
                user_profile.bio = bio
                user_profile.location = location
                user_profile.save()
            else:
                image = request.FILES.get('image')
                bio = request.POST['bio']
                location = request.POST['location']
                user_profile.profileimg = image
                user_profile.bio = bio
                user_profile.location = location
                user_profile.save()
            return redirect('/profile/' + id_user)
        else:
            return render(request, 'profile.html', context)
    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']
        if Followers.objects.filter(follower=follower, user=user).first():
            delete_follower = Followers.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user)
        else:
            new_follower = Followers.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user)
    else:
        return redirect('/')

@login_required(login_url='/login')
def delete(request, id):
    story = Story.objects.get(id=id)
    story.delete()
    return redirect('/profile/' + request.user.username)

@login_required(login_url='/login')
def search_results(request):
    query = request.GET.get('q')
    users = Profile.objects.filter(user__username__icontains=query)
    storiez = Story.objects.filter(caption__icontains=query)
    context = {
        'query': query,
        'users': users,
        'storiez': storiez,
    }
    return render(request, 'search-results.html', context)
