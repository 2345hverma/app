# Generated by Django 3.0.2 on 2020-01-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0009_auto_20200129_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminders',
            name='date_of_reminder',
            field=models.DateTimeField(),
        ),
    ]
