# Generated by Django 5.1.7 on 2025-03-27 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0002_remove_hospital_id_hospital_hospital_id'),
        ('insurancecompany', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_status_code', models.CharField(max_length=8)),
                ('status_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_number', models.IntegerField(primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('update_date', models.DateField()),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('insurance_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurancecompany.company')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('claim_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.claimstatus')),
            ],
        ),
    ]
