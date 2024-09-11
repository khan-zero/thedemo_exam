# Generated by Django 5.1 on 2024-09-11 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('start_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.position')),
            ],
        ),
        migrations.CreateModel(
            name='StaffAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.shift')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.staff')),
            ],
        ),
    ]
