# Generated by Django 5.1.7 on 2025-04-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurancecompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default='Not specified', upload_to='images/companies/'),
        ),
    ]
