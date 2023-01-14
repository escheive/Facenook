from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import SignUpForm, PostForm



# def Home(request):
#     posts = Post.objects.all()
#     print(posts[1].content)
#     return render(request, 'home.html', { 'posts': posts })


class Home(TemplateView):
    template_name = 'home.html'

    form = PostForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})


class About(TemplateView):
    template_name = 'about.html'

class MyProfile(TemplateView):
    template_name = 'my_profile.html'

def view_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "view_profile.html", {"profile": profile})

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
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = SignUpForm
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
