from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class HoursInput(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    hours_number = models.IntegerField(validators=[
        MaxValueValidator(15, "Niemożliwe, że tyle pracowałeś"),
        MinValueValidator(0, "Wprowadź liczbę dodatnią 0-15")
    ])
    workplace = models.CharField(max_length=100)


class WorkplaceInput(models.Model):
    workplace = models.CharField(max_length=100)

    def __str__(self):
        return self.workplace
