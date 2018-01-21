from django import forms
from ratings.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['beer_name', 'score', 'notes']

class RatingEditForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['id', 'beer_name', 'score', 'notes']

class RatingDeleteForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = []
