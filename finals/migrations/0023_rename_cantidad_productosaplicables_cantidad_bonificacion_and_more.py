# Generated by Django 4.2.6 on 2023-12-13 05:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("finals", "0022_remove_productosaplicables_articulo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productosaplicables",
            old_name="cantidad",
            new_name="cantidad_bonificacion",
        ),
        migrations.DeleteModel(
            name="PromocionArticuloBonificado",
        ),
    ]
