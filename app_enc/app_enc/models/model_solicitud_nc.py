from django.db import models

class SolicitudNC(models.Model):
    SOL_ID = models.AutoField(primary_key=True)
    SOL_FECHA_SOLICITUD = models.DateField()
    SOL_TIPO_NC = models.CharField(max_length=64)
    SOL_USUARIO_CREADOR = models.IntegerField()
    SOL_FECHA_CREACION = models.DateField(null=True)
    SOL_FECHA_MODIFICACION = models.DateField(null=True)
    SOL_ESTADO = models.CharField(max_length=64, null=True)
    SOL_OBSERVACION = models.TextField(null=True)
    SOL_USUARIO_VALIDADOR = models.IntegerField(null=True)
    class Meta:
        db_table="SOLICITUD_NC"