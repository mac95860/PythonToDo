from django.db import models

#create models here
class Todo(models.Model):
    added_date = models.dateTimeField()
    text = models.CharField(mas_length = 200)