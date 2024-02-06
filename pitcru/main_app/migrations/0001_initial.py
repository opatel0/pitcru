# Generated by Django 5.0.1 on 2024-02-06 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_mpg', models.IntegerField()),
                ('car_class', models.CharField(max_length=100)),
                ('combination_mpg', models.IntegerField()),
                ('cylinders', models.IntegerField()),
                ('displacement', models.FloatField()),
                ('drive', models.CharField(max_length=10)),
                ('fuel_type', models.CharField(max_length=10)),
                ('highway_mpg', models.IntegerField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('date', models.DateField(verbose_name='feeding date')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
