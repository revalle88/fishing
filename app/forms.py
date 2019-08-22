# -*- coding: utf-8 -*-
from django import forms

from .models import Pound, Review, Fish, Images
from django_summernote.widgets import SummernoteWidget


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

    # pound = forms.ModelChoiceField(queryset=Pound.objects.all(), required=False)
    rating = forms.IntegerField(initial=5, min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ('lat', 'lang', 'fishing_date', 'pound', 'content', 'fish_caught', 'rating')
        labels = {
            "fishing_date": "Когда была рыбалка:",
            'pound': "к какому водоему относится: ",
            'content': "Описание",
            'fish_caught': "Рыба поймана",
            'rating': "Рейтинг"
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['fish_caught'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["fish_caught"].help_text = ""
        self.fields["fish_caught"].queryset = Fish.objects.all()
        self.fields["lat"].widget = forms.widgets.HiddenInput()
        self.fields["lang"].widget = forms.widgets.HiddenInput()
        self.fields["fishing_date"].widget = forms.widgets.SelectDateWidget()


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image', )


