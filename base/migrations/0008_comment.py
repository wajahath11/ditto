# Generated by Django 4.2.5 on 2023-09-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_policy_medicals_status_alter_policy_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.policyprovider')),
            ],
        ),
    ]
