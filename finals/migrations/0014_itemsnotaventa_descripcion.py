# Generated by Django 4.2.6 on 2023-11-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finals', '0013_remove_itemsnotaventa_precio_unitario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsnotaventa',
            name='descripcion',
            field=models.JSONField(default=None),
        ),
    ]