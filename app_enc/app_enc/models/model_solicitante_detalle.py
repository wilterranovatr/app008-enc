from django.db import models

class SolicitanteDet(models.Model):
    SDET_ID = models.AutoField(primary_key=True)
    SDET_DNI = models.CharField(max_length=10)
    SDET_MATERNO = models.CharField(max_length=64)
    SDET_PATERNO = models.CharField(max_length=64)
    SDET_NOMBRES = models.CharField(max_length=64)
    class Meta:
        db_table ="SOLICITANTE_DET"