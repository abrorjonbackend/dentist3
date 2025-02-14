# Generated by Django 4.2.19 on 2025-02-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('birthDate', models.DateField()),
                ('address', models.TextField()),
                ('appointmentDate', models.DateField()),
                ('appointmentTime', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('givenPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('doctor', models.TextField()),
                ('tel', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
    ]
