from django import forms

class SearchListForm(forms.Form):
    name = forms.CharField(max_length=100)