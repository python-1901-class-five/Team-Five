from django.forms import ModelForm
from .models import Comment


class Commentform(ModelForm):
    class Meta():
        model = Comment
        fields = ['name', 'email', 'url', 'text']
