from django import forms
from .models import Food_Post

class FoodpostForm(forms.ModelForm):

    class Meta:
        model = Food_Post
        fields = (
            'title',
            'slug',
            'text',
            'publish',
        )