# Generated by Django 3.0.6 on 2022-11-08 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualapp', '0011_user_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='productor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='EstadoSolicitud',
            field=models.CharField(choices=[('1', 'Aprobado'), ('2', 'Rechazado'), ('3', 'Pendiente'), ('4', 'Subasta de transporte'), ('5', 'Transporte listo'), ('13', 'Entregado en bodega'), ('14', 'Entregado en bodega'), ('6', 'Revision de calidad'), ('7', 'Revisado'), ('8', 'En camino'), ('9', 'Viaje interrumpido'), ('10', 'Destino'), ('11', 'Rechazado'), ('12', 'Saldo')], default='3', max_length=50, null=True),
        ),
    ]
