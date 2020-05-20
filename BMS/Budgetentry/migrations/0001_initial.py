# Generated by Django 3.0.3 on 2020-05-05 18:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paymode', models.CharField(max_length=250, unique=True)),
                ('Username', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Essential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=250)),
                ('Username', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Amount', models.FloatField()),
                ('Dfield', models.DateField(default=datetime.date.today)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budgetentry.Essential')),
                ('Paymode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budgetentry.Account')),
            ],
        ),
    ]
