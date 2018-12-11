from django import forms
from django.forms import ModelForm
from .models import Commentary

class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ('text',)
