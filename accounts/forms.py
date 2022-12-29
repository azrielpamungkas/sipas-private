from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")

class NewPassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(NewPassword, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError("Password tidak sama")
        return cleaned_data


