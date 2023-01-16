from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


# return to this as stretch, adding additional values tied to user
# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = 

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