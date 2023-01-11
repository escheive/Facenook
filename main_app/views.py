from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Post
from django.contrib.auth import login
from .forms import SignUpForm




class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'


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
