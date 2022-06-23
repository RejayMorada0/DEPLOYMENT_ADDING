from email.policy import default
from django.db import models
from django.db.models import Model
import os
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Accounts
class registration(AbstractUser):
    section = [
        ('BET-COET-S-1A', 'BET-COET-S-1A'),
        ('BET-COET-NS-1B', 'BET-COET-NS-1B'),
        ('BET-COET-S-2A', 'BET-COET-S-2A'),
        ('BET-COET-NS-2B', 'BET-COET-NS-2B'),
        ('BET-COET-S-3A', 'BET-COET-S-3A'),
        ('BET-COET-NS-3B', 'BET-COET-NS-3B'),
        ('BET-COET-S-4A', 'BET-COET-S-4A'),
        ('BET-COET-NS-4B', 'BET-COET-NS-4B'),
    ]
    userType = [
        ('STDNT', 'Student'),
        ('DH', 'Department Head'),
        ('PIC', 'Person-in-charge'),
    ]
    
    section = models.CharField(max_length=30, choices= section, verbose_name='section')
    stud_id = models.IntegerField(unique=True, blank=True, null=True)
    stud_stats = models.CharField(max_length=30, default ='Processing')
    image = models.ImageField(max_length=100, default ='', upload_to='images')
    userType = models.CharField(max_length=30, choices= userType, verbose_name='userType', default ='STDNT')


#All Subjects
class all_subjects(models.Model):
    sub_code = models.CharField(max_length=100, unique=True)
    sub_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    offer_stats = models.CharField(max_length=100)
    

#Student Request
#foreign key (https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/)
#https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name
#https://stackoverflow.com/questions/2606194/django-error-message-add-a-related-name-argument-to-the-definition
class student_request(models.Model):
    stud_id = models.IntegerField(blank=True, null=True)
    sub_code = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    grades = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.CharField(max_length=100)
    offer_stats = models.CharField(max_length=100)


