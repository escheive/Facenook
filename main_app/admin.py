from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post, Profile, Comment




class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]




# Unregister the default django groups
admin.site.unregister(Group)
# Unregister and re-register User to change what is displayed from Django's default settings
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)