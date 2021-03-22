# Date Started: March 20, 2021
# Author/s: Wylen Joan Lee

# References:
# 

from django import forms
from .models import RegularUser
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    gender = forms.CharField(required=False)

    class Meta:
        model = RegularUser
        fields = ['user_id','gender',]
        
## newly added
class UserForm(UserCreationForm):
	class Meta:
		model = user
		fields = ['first_name','last_name','gender', 'email', 'password']

class EventsForm(UserCreationForm):
	class Meta:
		model = event
		fields = ['title','description','event_type','start_date','end_date','start_time','end_time','status','upvotes_count']