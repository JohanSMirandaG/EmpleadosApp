# Generated by Django 4.2.4 on 2023-09-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_remove_habilidades_hability_empleado_abilities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilidades',
            name='ability',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, verbose_name='ability'),
        ),
    ]
