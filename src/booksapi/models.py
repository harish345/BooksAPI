"""
Created on June 29, 2019

@author: harish345

"""
from django.db import models
from django_mysql import models as m
# Model class for Books table
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=128,unique=True, null=False)
    isbn=models.CharField(max_length=256,null=False)
    authors=m.ListCharField(
        base_field=models.CharField(max_length=10),
        null=False,
        max_length=128)
    country=models.CharField(max_length=128,null=False)
    number_of_pages=models.IntegerField(null=False)
    publisher=models.CharField(max_length=128,null=False)
    release_date=models.DateField()
    
    class Meta:
        db_table = 'books'