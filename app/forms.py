# -*- coding: utf-8 -*-
from django import forms

from .models import Pound, Review, Fish
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PoundForm(forms.ModelForm):

    class Meta:
        model = Pound
        fields = (
            'lat', 'lang', 'name', 'description', 'fishes', 'is_paid',  'contacts', 'conditions'
        )

        widgets = {
            'description': SummernoteWidget()
        }


class ReviewForm(forms.ModelForm):

    pound = forms.ModelChoiceField(queryset=Pound.objects.all(), required=False)

    class Meta:
        model = Review
        fields = ('lat', 'lang', 'fishing_date', 'pound', 'content', 'fish_caught', 'rating')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['fish_caught'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["fish_caught"].help_text = ""
        self.fields["fish_caught"].queryset = Fish.objects.all()


# class PointForm(forms.Form):
#     birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     lat = forms.FloatField()
#     lang = forms.FloatField()
#     fishing_date = forms.DateField()
#     fish_caught = self.fields["diets"].widget = forms.widgets.CheckboxSelectMultiple()
#     favorite_colors = forms.MultipleChoiceField(required=False,
#         widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

