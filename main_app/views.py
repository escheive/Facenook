from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Comment
from .forms import SignUpForm, PostForm, CommentForm, EditUserForm


@login_required
def dashboard(request):
    followed_posts = Post.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main_app:dashboard')

    
    return render(request, 'dashboard.html', {'posts': followed_posts, 'form': form })




def home(request):
    posts = Post.objects.all().order_by("-created_at")

    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main_app:home')

    
    return render(request, 'home.html', {'posts': posts, 'form': form})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, "profile_list.html", {"profiles": profiles})

def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post.id)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return render('main_app:view_post', pk=post.id)

    return render(request, 'view_post.html', { 'post': post, 'comments': comments, 'form': form })

def delete_post(request, pk):

    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('main_app:view_profile', pk=request.user.profile.id)

    return render(request, 'delete_post.html')

def view_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        print('-------------------------------------------------------------------------------Reached here')
        if form.is_valid():
           

            comment.user = request.user
            comment = form.save(commit=False)
            comment.save()
            return redirect('view_post.html')


    return render(request, 'view_comment.html', { 'comment': comment, 'form': form })


class About(TemplateView):
    template_name = 'about.html'

def view_profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()


    profile = Profile.objects.get(pk=pk)
    user_posts = Post.objects.filter(user=profile.user).order_by('-created_at')

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main_app:view_profile', pk=profile.id)

    return render(request, "view_profile.html", {"profile": profile, 'form': form, 'user_posts': user_posts})

def edit_profile(request, pk):

    profile = Profile.objects.get(pk=pk)
    user_posts = Post.objects.filter(user=profile.user).order_by('-created_at')

    if request.POST:
        form = EditUserForm(request.POST, instance=profile.user)
        if form.is_valid():
            messages.success(request, 'Your profile is updated successfully')
            user = form.save()
            profile = form.save()
            return redirect('main_app:view_profile', pk=user.profile.id)
    else:
        form = EditUserForm(instance=profile.user)

    return render(request, "edit_profile.html", {"profile": profile, 'user_posts': user_posts, 'form': form})

def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        profile.delete()
        return redirect('main_app:home')

    return render(request, 'delete_post.html')

class CreatePost(CreateView):
    model = Post 
    fields = ['user', 'content']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('/')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = SignUpForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      profile = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('{% url main_app:dashboard.html %}')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = SignUpForm
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
