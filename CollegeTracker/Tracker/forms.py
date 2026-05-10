from django import forms
from django.forms import inlineformset_factory
from .models import userprofile, APScore


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userprofile
        exclude = ['user']
        widgets = {
            # Geographic
            'State': forms.TextInput(attrs={'placeholder': 'e.g. California'}),
            'City': forms.TextInput(attrs={'placeholder': 'e.g. San Diego'}),
            'School': forms.TextInput(attrs={'placeholder': 'High school name'}),

            # GPA — step lets users enter decimals like 3.85
            'OverallGPA': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'FreshGPAUW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'FreshGPAU': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'SophGPAUW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'SophGPAW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'JunGPAUW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'JunGPAW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'SenGPAUW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),
            'SenGPAW': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 5}),

            # Test scores
            'SAT': forms.NumberInput(attrs={'min': 400, 'max': 1600, 'placeholder': '400 - 1600'}),
            'ACT': forms.NumberInput(attrs={'min': 1, 'max': 36, 'placeholder': '1 - 36'}),
        }


# Inline formset for AP scores tied to a userprofile.
# `extra=5` shows 5 blank rows for adding new scores; `can_delete=True` adds a
# delete checkbox to existing rows.
APScoreFormSet = inlineformset_factory(
    userprofile,
    APScore,
    fields=['exam_name', 'score'],
    extra=1,          # one blank row to start; "Add Exam" button creates more
    can_delete=True,
)
