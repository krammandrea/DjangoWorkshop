from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0) 

    # whenever an Author object is printed 
    def __unicode__(self):
        return self.name
