# Generated by Django 4.2.5 on 2023-09-05 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_policy_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='medicals_status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Scheduled', 'Scheduled'), ('WaitingForReport', 'Waiting for Report'), ('Done', 'Done')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='remarks',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(200)]),
        ),
    ]
