# Generated by Django 3.1.2 on 2020-12-28 16:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0002_hoursinput_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoursinput',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hoursinput',
            name='hours_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(15, 'Niemożliwe, że tyle pracowałeś'), django.core.validators.MinValueValidator(0, 'Wprowadź liczbę dodatnią 0-15')]),
        ),
    ]
