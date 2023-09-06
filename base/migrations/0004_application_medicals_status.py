# Generated by Django 4.2.5 on 2023-09-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_name_application_customer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='medicals_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Scheduled', 'Scheduled'), ('WaitingForReport', 'Waiting for Report'), ('Done', 'Done')], default='Pending', max_length=20),
            preserve_default=False,
        ),
    ]