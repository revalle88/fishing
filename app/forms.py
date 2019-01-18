from django import forms

from .models import Pound


class PoundForm(forms.ModelForm):

    class Meta:
        model = Pound
        fields = ('name', 'description',)
