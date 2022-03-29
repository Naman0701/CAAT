# Generated by Django 3.2.7 on 2022-01-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('Sub_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Sub_name', models.CharField(max_length=50)),
                ('Dept', models.CharField(max_length=50)),
                ('Sem', models.IntegerField()),
                ('Credits', models.IntegerField()),
            ],
        ),
    ]