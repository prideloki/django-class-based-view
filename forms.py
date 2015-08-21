from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(label='Name',max_length=50)
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='Age')