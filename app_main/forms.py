from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'tags']
        # fields = ['title', 'description', 'image', 'tags', 'source_link', 'demo_link']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'input'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'input'
            }),
            'source_link': forms.URLInput(attrs={
                'class': 'input'
            }),
            'demo_link': forms.URLInput(attrs={
                'class': 'input'
            })
        }
