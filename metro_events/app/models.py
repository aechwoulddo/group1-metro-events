# Date Started: March 20, 2021
# Author/s: Wylen Joan Lee

# References:
#   https://docs.djangoproject.com/en/3.1/ref/models/fields/
#   https://docs.djangoproject.com/en/3.1/topics/db/queries/#backwards-related-objects

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class RegularUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length = 6, blank = True, null = True)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "User"

class OrganizerUser(models.Model):
    regular_user_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE, related_name='organizers')
    granted_at = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = "Organizer"

class AdministratorUser(models.Model):
    regular_user_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE, related_name='administrators')
    granted_at = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = "Administrator"

## newly added 
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "user"
        
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    event_type = models.CharField(max_length=200, null=True)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    status = models.CharField(max_length=200, null=True)
    upvotes_count = models.IntegerField(default=0)

    class Meta:
        db_table = "event"