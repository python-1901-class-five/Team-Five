from django import forms
class AddForm(forms.Form):
    username = forms.CharField(max_length=20)
    age = forms.IntegerField()