from django.db import models

class RolesPermisos(models.Model):
    RPER_ID = models.AutoField(primary_key=True)
    ROL_ID = models.IntegerField()
    PER_ID = models.IntegerField()
    class Meta:
        db_table="ROLES_PERMISOS"