# Generated by Django 4.2.6 on 2023-12-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finals", "0033_remove_promocion_condiciones_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="promocion",
            name="monto_maximo",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=10, null=True
            ),
        ),
    ]
