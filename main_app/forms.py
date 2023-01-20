from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import PasswordInput, TextInput
from .models import Post, Comment, Profile





class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']:
            self.fields['username'].widget = TextInput(
                attrs={
                    'placeholder': 'Username', 
                    'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
            self.fields['email'].widget = TextInput(
                attrs={
                    'placeholder': 'Email', 
                    'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
            self.fields['first_name'].widget = TextInput(
                attrs={
                    'placeholder': 'First Name', 
                    'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
            self.fields['last_name'].widget = TextInput(
                attrs={
                    'placeholder': 'Last Name', 
                    'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
            self.fields['password1'].widget = PasswordInput(
                attrs={
                    'placeholder': 'Password', 
                    'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
            self.fields['password2'].widget = PasswordInput(
                attrs={
                    'placeholder': 'Confirm Password',
                    'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')





class EditUserForm(forms.ModelForm):

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