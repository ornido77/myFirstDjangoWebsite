from django import forms

class createNewNote(forms.Form):
    name = forms.CharField(label="Name", max_length=250)
    check = forms.BooleanField()
