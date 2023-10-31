from django.db import models

class DetalleSolicitud(models.Model):
    DET_ID = models.AutoField(primary_key=True)
    DET_FECHA_EMISION = models.DateField()
    DET_NRO_COMPROBANTE = models.CharField(max_length=64)
    DET_IMPORTE_TOTAL = models.FloatField()
    DET_MOTIVO = models.CharField(max_length=255, null=True)
    DET_MONTO_TOTAL_PROD = models.FloatField(null=True)
    DET_ESTABLECIMIENTO = models.IntegerField(null=True)
    DET_DESCUENTO = models.IntegerField(null=True)
    DET_TOTAL_DESCUENTO = models.FloatField(null=True)
    DET_BOLETEO = models.FloatField(null=True)
    SDET_ID = models.IntegerField(null=True)
    DET_LABORA_EN = models.CharField(max_length=64, null=True)
    class Meta:
        db_table="DETALLE_SOLICITUD"