from django import forms  # Is has the functionality to be connected to some model

from app_main.models import Profile, Skill
from app_users.models import Message


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        # fields = ['first_name', 'last_name', 'short_intro', 'bio']
        exclude = ['user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input',
            }),
            'short_intro': forms.TextInput(attrs={
                'class': 'input',
            }),
            'location': forms.TextInput(attrs={
                'class': 'input',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'input'
            }),
            'social_github': forms.URLInput(attrs={
                'class': 'input'
            }),
            'social_facebook': forms.URLInput(attrs={
                'class': 'input'
            }),
            'social_instagram': forms.URLInput(attrs={
                'class': 'input'
            }),
            'social_telegram': forms.URLInput(attrs={
                'class': 'input'
            }),
            'social_website': forms.URLInput(attrs={
                'class': 'input'
            }),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        # fields = []
        exclude = ['owner']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'input',
            }),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fullname', 'email', 'subject', 'body']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'input',
                'required': 'true',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'required': 'true',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'input'
            }),
            'body': forms.Textarea(attrs={
                'class': 'input'
            }),
        }
