# Generated by Django 3.0.6 on 2022-11-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualapp', '0018_auto_20221108_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='posthistorico',
            name='contenido',
            field=models.CharField(max_length=50, null=True),
        ),
    ]