from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    due_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    def d_day(self):
        d_day = self.due_date - date.today()
        return d_day.days