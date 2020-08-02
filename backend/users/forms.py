from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = UserChangeForm.Meta.fields
