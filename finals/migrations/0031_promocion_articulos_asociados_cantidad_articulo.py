# Generated by Django 4.2.6 on 2023-12-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finals", "0030_remove_articulo_factor_compra_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocion_articulos_asociados",
            name="cantidad_articulo",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
