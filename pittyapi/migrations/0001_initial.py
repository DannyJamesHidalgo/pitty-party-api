# Generated by Django 5.0.7 on 2024-07-22 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('health_status', models.CharField(max_length=100)),
                ('story', models.TextField()),
                ('adoption_status', models.CharField(max_length=20)),
                ('arrival_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PittyParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pittyapi.adopter')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pittyapi.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adoption_date', models.DateField()),
                ('adoption_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pittyapi.adopter')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pittyapi.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Fostering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pittyapi.dog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('treatment', models.TextField()),
                ('veterinarian', models.CharField(max_length=255)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pittyapi.dog')),
            ],
        ),
    ]
