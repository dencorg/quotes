# Generated by Django 2.2.6 on 2019-10-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
