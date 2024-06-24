from django.contrib import admin
from .models import Profile, Story, LikeStory, Followers


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_user', 'bio', 'location')  # Example fields to display in the admin list view


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'caption', 'created_at', 'no_of_likes', 'image')  # Example fields to display in the admin list view
    list_filter = ('category', 'created_at')  # Example filters in the admin list view
    search_fields = ('user', 'caption', 'short_description', 'full_description')


# @admin.register(LikeStory)
# class LikeStoryAdmin(admin.ModelAdmin):
#     list_display = ('username', 'post', 'created_at')  # These should match the fields in the model
#     list_filter = ('created_at',)  # Ensure 'created_at' is a valid field in the model


admin.site.register(LikeStory)
admin.site.register(Followers)
