# Generated by Django 4.2 on 2025-06-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicauthorization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
