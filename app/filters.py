import django_filters
from django_filters import DateRangeFilter
from django_filters.widgets import RangeWidget
from django import forms

from .models import Review, Fish, Method


class ReviewFilter(django_filters.FilterSet):
    method = django_filters.ModelMultipleChoiceFilter(
        queryset=Method.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    fish_caught = django_filters.ModelMultipleChoiceFilter(
        queryset=Fish.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    fishing_date = DateRangeFilter()



    class Meta:
        model = Review
        fields = ['method', 'fish_caught', 'pound', 'fishing_date']


