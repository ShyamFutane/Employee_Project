from django.db import models


# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
