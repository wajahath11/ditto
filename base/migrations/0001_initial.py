# Generated by Django 4.2.5 on 2023-09-05 14:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FieldRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('is_required', models.BooleanField(default=True)),
                ('scenario', models.CharField(max_length=100)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.policyprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_number', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('policy_cover', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(2500000, message='Policy cover must be at least 25L'), django.core.validators.MaxValueValidator(50000000, message='Policy cover cannot exceed 5cr')])),
                ('policy_status', models.CharField(choices=[('Awaited', 'Requirements Awaited'), ('Closed', 'Requirements Closed'), ('Underwriting', 'Underwriting'), ('PolicyIssued', 'Policy Issued'), ('PolicyRejected', 'Policy Rejected')], max_length=20)),
                ('policy_number', models.CharField(blank=True, max_length=50, null=True)),
                ('medical_type', models.CharField(blank=True, choices=[('TeleMedicals', 'Tele Medicals'), ('PhysicalMedicals', 'Physical Medicals')], max_length=20, null=True)),
                ('remarks', models.TextField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(200)])),
                ('policy_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.policyprovider')),
            ],
        ),
    ]