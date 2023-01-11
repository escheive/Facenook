from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


# return to this as stretch, adding additional values tied to user
# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = 