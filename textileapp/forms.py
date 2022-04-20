from django import forms
from django.contrib.auth.models import User
from . import models
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class BuyerForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class Bills(forms.Form):
    Name = forms.CharField(max_length=20)
    # Price = forms.IntegerField()
    Address =forms.CharField(max_length=40)
    Phone =  forms.IntegerField()
    Quantity = forms.IntegerField()