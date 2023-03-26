from distutils.command.build_scripts import first_line_re
from django.contrib.auth.models import AbstractUser 
from django.db import models
class Developer(AbstractUser):
 first_name = models.CharField("first name", max_length=200)
 last_name = models.CharField(max_length=200)
 REQUIRED_FIELDS=['first_name', 'last_name','password'] 

 def __str__(self):
      return f"{self.first_name} {self.last_name}"
 def is_free(self):
      return self.tasks.count() == 0
 is_free.boolean = True 
 is_free.short_description = 'Is free' 
