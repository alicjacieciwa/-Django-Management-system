from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class HoursInput(models.Model):
    date = models.DateField(default=datetime.date.today)
    hours_number = models.IntegerField(validators=[
        MaxValueValidator(15, "Niemożliwe, że tyle pracowałeś"),
        MinValueValidator(0, "Wprowadź liczbę dodatnią 0-15")
    ])
    workplace = models.CharField(max_length=100)

