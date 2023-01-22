from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Profile, Comment, User
from .forms import SignUpForm, PostForm, CommentForm, EditUserForm




# View for the main page before signing up or logging in
def home(request):

    return render(request, 'home.html')



# View for the dashboard page
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



# View for the explore page
@login_required
def explore(request):
    posts = Post.objects.all().order_by("-created_at")

    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main_app:explore')

    
    return render(request, 'explore.html', {'posts': posts, 'form': form})



# View for the profile list page
@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, "profile_list.html", {"profiles": profiles})



# View for viewing a users post
@login_required
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
            return redirect('main_app:view_post', pk=post.id)

    return render(request, 'view_post.html', { 'post': post, 'comments': comments, 'form': form })



# View for deleting a post
@login_required
def delete_post(request, pk):

    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('main_app:view_profile', pk=request.user.profile.id)

    return render(request, 'delete_post.html')



# View for viewing a comment
@login_required
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



# View for viewing a user profile
@login_required
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



# View for editing a profile
@login_required
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


# View for deleting a users acct
@csrf_exempt
def delete_profile(request, pk):

    # grab the profile from the database
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        # grab the user
        user = User.objects.get(profile=profile)
        # delete the user
        user.delete()
        # send a confirmation message
        messages.success(request, 'Your profile has been deleted successfully')
        # redirect back to the home page
        return redirect('main_app:home')

    return render(request, 'delete_profile.html')



# View for creating a post
@login_required
class CreatePost(CreateView):
    model = Post 
    fields = ['user', 'content']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('/')



# View for the User signup page
def signup(request):
  
    form = SignUpForm()

    if request.method == 'POST':

        # This is how to create a 'user' form object, that includes the data from the browser
        form = SignUpForm(request.POST)

        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            # redirect user to their dashboard after they are signed up and logged in
            return redirect('/dashboard')

    else:
        # A GET or a bad POST request, so render signup.html with an empty form
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})
