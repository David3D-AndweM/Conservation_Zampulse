from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Profile, Story, LikeStory


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fmn')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')

        try:
            # Check if user already exists
            if User.objects.filter(username=fnm).exists() or User.objects.filter(email=emailid).exists():
                invalid = "User Already Exists"
                return render(request, 'signup.html', {'invalid': invalid})

            my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            my_user.save()

            new_profile = Profile.objects.create(user=my_user, id_user=my_user.id)
            new_profile.save()

            login(request, my_user)
            return redirect('/')

        except Exception as e:
            invalid = f"An error occurred: {str(e)}"
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


def logoutt(request):
    logout(request)
    return redirect('/loginn')


def home(request):
    story = Story.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    context = {
        'story': story,
        'Profile': profile,
    }
    return render(request, 'main.html', context)


def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image-upload')
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


def likes(request, id):
    if request.method == 'GET':  # Corrected 'Get' to 'GET'
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


def home_story(request, id):
    story = Story.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'story': story,
        'profile': profile,
    }

    return render(request, 'main.html', context)


def explore(request):
    stories = Story.objects.all().order_by('-created_at')  # Corrected ordering by 'created_at'
    profile = Profile.objects.get(user=request.user)
    context = {
        'stories': stories,  # Renamed 'story' to 'stories' for clarity (plural form)
        'profile': profile,
    }
    return render(request, 'explore.html', context)


def profile(request, id_user):
    user_object = User.objects.get(username=id_user)
    profile = Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_stories = Story.objects.filter(user=id_user).order_by('-created_at')
    user_stories_length = len(user_stories)
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_stories': user_stories,
        'user_stories_length': user_stories_length,
        'profile': profile,
    }

    if request.user.username == id_user:
        if request.method == 'POST':
            if request.FILES.get('image') == None:
                image = user_profile.profileimg
                bio = request.POST['bio']
                location = request.POST['location']

                user_profile.profileimg = image
                user_profile.bio = bio
                user_profile.location = location
                user_profile.save()
            if request.FILES.get('image') != None:
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
