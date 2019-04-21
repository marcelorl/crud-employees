from django.db import models
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    created_on = models.DateField(default=date.today)

    class Meta:
        db_table = 'employee'
        ordering = ['id']

    def __str__(self):
        return self.name
