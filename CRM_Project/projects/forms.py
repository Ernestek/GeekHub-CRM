from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Check if the owner is not in the user list
        if cleaned_data.get('owner') in cleaned_data.get('users').all():
            raise ValidationError({'users': _('Owner cannot be in the users list.')})

        return self.cleaned_data
