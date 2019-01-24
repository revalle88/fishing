from django import forms

from .models import Pound, Review


class PoundForm(forms.ModelForm):

    class Meta:
        model = Pound
        fields = ('name', 'description', 'fishes')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('fishing_date', 'pound', 'content', 'fish_caught', 'rating')
