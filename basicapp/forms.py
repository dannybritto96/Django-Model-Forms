from django import forms

from .models import Details

class DetailsForm(forms.ModelForm):

        class Meta:
            model = Details
            fields = ('name','email')

        name = forms.CharField(max_length=100,label="Enter Name:")
        email = forms.EmailField(max_length=150,label="Enter Email:")
