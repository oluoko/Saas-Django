from django.db import models

# Create your models here.
class PageVisit(models.Model): 
    # db -> table
    # id -> primary key -> auto increment
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)