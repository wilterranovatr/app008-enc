from django.db import models

class ProductoDetalle(models.Model):
    DPRO_ID = models.AutoField(primary_key=True)
    DPRO_CODIGO = models.CharField(max_length=7)
    DPRO_DESCRIPCION = models.CharField(max_length=255)
    DPRO_UNIDAD = models.CharField(max_length=32)
    DPRO_PRECIO = models.FloatField()
    DPRO_CANTIDAD = models.IntegerField()
    DPRO_MONTO_TOTAL = models.FloatField()
    class Meta:
        db_table="PRODUCTO_DETALLE"