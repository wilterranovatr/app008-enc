from django.db import models

class Market(models.Model):
    MAR_ID = models.AutoField(primary_key=True)
    MAR_DESCRIPCION = models.CharField(max_length=64)
    class Meta:
        db_table="MARKET"