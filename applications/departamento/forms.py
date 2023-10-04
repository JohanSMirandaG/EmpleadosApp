from django import forms

class NewDepartmentForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    department = forms.CharField(max_length=50, required=True)
    shorname = forms.CharField(max_length=20, required=True)