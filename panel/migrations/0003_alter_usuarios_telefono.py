# Generated by Django 5.0 on 2024-02-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_usuarios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='Telefono',
            field=models.BigIntegerField(),
        ),
    ]