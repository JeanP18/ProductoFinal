# Generated by Django 4.2.6 on 2023-12-13 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("finals", "0020_rename_codigo_sku_promocion_articulo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="promocion",
            name="articulo",
        ),
        migrations.RemoveField(
            model_name="promocion",
            name="cantidad",
        ),
        migrations.AddField(
            model_name="promocion",
            name="cantidad_minima_compra",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="promocion",
            name="condiciones",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="promocion",
            name="descuentos",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="promocion",
            name="formula",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="promocion",
            name="monto_maximo",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="promocion",
            name="monto_minimo",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="promocion",
            name="porcentaje_descuento",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="promocion",
            name="proveedor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="promociones",
                to="finals.gruposproveedor",
            ),
        ),
        migrations.AddField(
            model_name="promocion",
            name="tipo_promocion",
            field=models.CharField(
                choices=[
                    ("Descuento", "Descuento"),
                    ("Descuento_Proveedor", "Descuento por Proveedor"),
                    ("Descuento_Rango", "Descuento por Rango de Compra"),
                    ("Descuento_Monto", "Descuento por Monto Total"),
                    ("Descuento_Cantidad", "Descuento por Cantidad Comprada"),
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
                default=1,
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="promocion",
            name="unidades_bonificadas",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="promocion",
            name="activo",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="promocion",
            name="descripcion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="promocion",
            name="fecha_fin",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="promocion",
            name="fecha_inicio",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="promocion",
            name="tipo_cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="promociones",
                to="finals.canalcliente",
            ),
        ),
        migrations.CreateModel(
            name="PromocionArticuloBonificado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.PositiveIntegerField()),
                (
                    "articulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finals.articulo",
                    ),
                ),
                (
                    "promocion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finals.promocion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductosAplicables",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "articulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finals.articulo",
                    ),
                ),
                (
                    "promocion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finals.promocion",
                    ),
                ),
            ],
        ),
    ]