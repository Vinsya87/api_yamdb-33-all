# Generated by Django 2.2.16 on 2022-04-07 18:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220407_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Оценка'),
        ),
    ]