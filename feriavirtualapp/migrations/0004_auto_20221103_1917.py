# Generated by Django 3.0.6 on 2022-11-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualapp', '0003_auto_20221024_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imagen',
            field=models.ImageField(default='perfil/default.png', upload_to='Perfil'),
        ),
    ]