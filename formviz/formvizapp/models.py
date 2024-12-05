from django.db import models

class MapRowSec(models.Model):
    usr_access = models.CharField(max_length=255)
    param = models.CharField(max_length=255)
    paramvalue = models.CharField(max_length=255)
    dashboard_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'map_rowsec' 
        managed = False  
    def __str__(self):
        return self.usr_access