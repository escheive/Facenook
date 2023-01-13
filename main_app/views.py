from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import SignUpForm



# def Home(request):
#     posts = Post.objects.all()
#     print(posts[1].content)
#     return render(request, 'home.html', { 'posts': posts })


class Home(TemplateView):
    template_name = 'home.html'

    def get_queryset(self):
        posts = Post.objects.all()
        return posts

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
        


class About(TemplateView):
    template_name = 'about.html'

class Profile(TemplateView):
    template_name = 'profile.html'


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
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = SignUpForm
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
