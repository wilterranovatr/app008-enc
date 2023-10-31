from django.db import models

class Roles(models.Model):
    ROL_ID = models.AutoField(primary_key=True)
    ROL_CODIGO = models.CharField(max_length=5)
    ROL_DESCRIPCION = models.CharField(max_length=32)
    class Meta:
        db_table="ROLES"