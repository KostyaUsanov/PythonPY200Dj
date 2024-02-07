from django import forms


class MyForm(forms.Form):
    my_name = forms.CharField(),
    my_email = forms.EmailField(),
    my_message = forms.CharField()

