from django.db import models

class Permisos(models.Model):
    PER_ID = models.AutoField(primary_key=True)
    PER_CODIGO = models.CharField(max_length=5)
    PER_DESCRIPCION = models.CharField(max_length=32)
    class Meta:
        db_table="PERMISOS"