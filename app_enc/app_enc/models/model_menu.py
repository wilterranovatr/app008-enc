from django.db import models

class Menu(models.Model):
    MEN_ID = models.AutoField(primary_key=True)
    MEN_DESCRIPCION = models.CharField(max_length=32)
    class Meta:
        db_table="MENU"