# Generated by Django 3.2.2 on 2024-10-01 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectofinalpp', '0008_alter_venta_total_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='id_Empleados',
        ),
        migrations.AddField(
            model_name='caja',
            name='empleado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyectofinalpp.empleado'),
            preserve_default=False,
        ),
    ]
