# Generated by Django 3.2.7 on 2022-01-23 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_auto_20220122_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aictep',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 1, 23)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 1, 23)),
        ),
    ]
