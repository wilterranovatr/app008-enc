from django.db import models

class MenuRPermisos(models.Model):
    MERP_ID = models.AutoField(primary_key=True)
    MEN_ID = models.IntegerField()
    RPER_ID = models.IntegerField()
    class Meta:
        db_table="MENU_RPERMISOS"