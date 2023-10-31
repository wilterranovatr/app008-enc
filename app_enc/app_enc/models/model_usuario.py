from django.db import models

class Usuario(models.Model):
    USU_ID = models.AutoField(primary_key=True)
    USU_NOMBRE = models.CharField(max_length=32)
    USU_CORREO = models.CharField(max_length=64, null=True)
    MAR_ID = models.IntegerField(null=True)
    ROL_ID = models.IntegerField(null=True)
    class Meta:
        db_table="USUARIO"