from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import PasswordInput, TextInput
from .models import Post, Comment, Profile




# Form for creating a user account
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

    def clean(self):
        cleaned_data=super().clean()
        # check if username is already taken
        if User.objects.filter(username=cleaned_data['username']).exists():
            raise ValidationError("That username is already taken")

        # grab password from form
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data.get('password2')
        # validate password
        min_length = 8
        if len(password1) < min_length:
            raise ValidationError('Password must be at least %s characters long.' %(str(min_length)))

        # check for digit
        if sum(c.isdigit() for c in password1) < 1:
            raise ValidationError('Password must contain at least 1 number.')

        # check for uppercase letter
        if not any(c.isupper() for c in password1):
            raise ValidationError('Password must contain at least 1 uppercase letter.')

        # check for lowercase letter
        if not any(c.islower() for c in password1):
            raise ValidationError('Password must contain at least 1 lowercase letter.')

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("The two password fields must match.")
        return cleaned_data

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')





class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
                self.fields['username'].widget = TextInput(
                    attrs={
                        'placeholder': 'Username', 
                        'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
                self.fields['password1'].widget = PasswordInput(
                    attrs={
                        'placeholder': 'Password', 
                        'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"})
                self.fields[fieldname].help_text = None
                self.fields[fieldname].label = ''
                






# Form for editing a users acct
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




# Form for posting content
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




# Form for posting a comment on a post
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