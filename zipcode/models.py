from django.db import models
from django import forms
class Zip_code(models.Model):
    post_office_name=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=10)
    district_name=models.CharField(max_length=50)
    city_name=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    def __unicode__(self):
        return self.post_office_name
# Create your models here.

# Create your models here.
