# Generated by Django 4.2.4 on 2023-08-31 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('shor_name', models.CharField(blank=True, max_length=20, verbose_name='shor_name')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
        ),
    ]