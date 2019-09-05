# -*- coding: utf-8 -*-
from django import forms
from django.utils.timezone import now

from .models import Pound, Review
from django_summernote.widgets import SummernoteWidget
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import DateField


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
    # rating = forms.IntegerField(initial=5, min_value=1, max_value=5)
    fishing_date = DateField(input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], initial=now().date())

    class Meta:
        model = Review
        fields = (
            'lat',
            'lang',
            'fishing_date',
            'fish_caught',
            'picture',
            'method',
            'content',
            'length',
            'weight',
            'pound'
        )
        labels = {
            "fishing_date": "Когда была рыбалка:",
            'pound': "Водоем",
            'content': "Описание",
            'fish_caught': "Рыба поймана",
            'weight': "Вес",
            'length': 'Длина',
            'picture': 'Прикрепить фото'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["fish_caught"].help_text = ""
        self.fields["lat"].widget = forms.widgets.HiddenInput()
        self.fields["lang"].widget = forms.widgets.HiddenInput()
        self.fields["fishing_date"].widget = DatePickerInput(format='%m/%d/%Y')
