from django.db import models
import datetime


class HoursInput(models.Model):
    date = models.DateField(default=datetime.date.today)
    hours_number = models.IntegerField()
    workplace = models.CharField(max_length=100)

