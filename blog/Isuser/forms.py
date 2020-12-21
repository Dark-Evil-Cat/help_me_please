from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, UserCreationForm
from Test.models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


class AuthUserLogin(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User
        fields = ("username", "password")

