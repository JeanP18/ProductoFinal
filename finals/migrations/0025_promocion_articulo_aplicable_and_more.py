# Generated by Django 4.2.6 on 2023-12-13 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("finals", "0024_remove_productosaplicables_cantidad_bonificacion"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocion",
            name="articulo_aplicable",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="productos_aplicables",
                to="finals.articulo",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="promocion",
            name="articulo_bonificacion",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="productos_bonificacion",
                to="finals.articulo",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="promocion",
            name="tipo_promocion",
            field=models.CharField(
                choices=[
                    ("caso_1", "Descuento por Cantidad Comprada (caso 1)"),
                    ("Descuento_Proveedor", "Descuento por Proveedor"),
                    ("Descuento_Rango", "Descuento por Rango de Compra"),
                    ("Descuento_Monto", "Descuento por Monto Total"),
                    ("Bonificacion", "Bonificación"),
                    ("Bonificacion_Cantidad", "Bonificación por Cantidad Comprada"),
                    ("Bonificacion_Monto", "Bonificación por Monto Total"),
                    ("Bonificacion_Proveedor", "Bonificación por Proveedor"),
                    ("Bonificacion_Rango", "Bonificación por Rango de Compra"),
                    ("Regalo", "Regalo con Compra"),
                    ("Regalo_Cantidad", "Regalo por Cantidad Comprada"),
                    ("Regalo_Monto", "Regalo por Monto Total"),
                    ("Regalo_Proveedor", "Regalo por Proveedor"),
                    ("Regalo_Rango", "Regalo por Rango de Compra"),
                ],
                max_length=50,
            ),
        ),
        migrations.DeleteModel(
            name="ProductosAplicables",
        ),
    ]
