from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post, Comment, Profile

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class EditUserForm(forms.ModelForm):
    # def __init__(self, **kwargs):
    #     self.username = kwargs.pop('username', None)
    #     self.email = kwargs.pop('email', None)
    #     self.first_name = kwargs.pop('first_name', None)
    #     self.last_name = kwargs.pop('last_name', None)
    #     super(EditUserForm, self).__init__(**kwargs)

    username = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'name': '',
                'required': 'True',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }
        )
    )

    email = forms.CharField(max_length=100, 
    required=False,
    widget=forms.widgets.TextInput(
            attrs={
                'name': '',
                'required': 'True',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }
        )
    )

    first_name = forms.CharField(
    max_length=100, 
    required=False,
    widget=forms.widgets.TextInput(
        attrs={
            'name': '',
            'required': 'True',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }
    )
    )
    last_name = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'name': '',
                'required': 'True',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        exclude = ('password1', 'password2')



class PostForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Write your thoughts',
                'class': 'w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400'
            }
        ),
        label=""
    )

    class Meta:
        model = Post
        fields = ('content', )
        exclude = ("user", )

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Write your thoughts',
                'class': 'form-control w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400'
            }
        ),
        label=""
    )

    class Meta:
        model = Comment
        fields = ('content', 'parent')
        exclude = ("user", )