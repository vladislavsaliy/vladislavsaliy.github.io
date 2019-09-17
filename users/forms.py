from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserOurRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username', 'email']


class ProfileImageUpdate(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImageUpdate, self).__init__(*args, **kwards)
        self.fields['img'].label = 'Image of profile'

    class Meta:
        model = Profile
        fields =['img']