# Generated by Django 3.1.4 on 2020-12-08 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
