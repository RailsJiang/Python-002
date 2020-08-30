from django.db import models

# Create your models here.


class T1(models.Model):
    n_star = models.IntegerField(blank=True, null=True)
    short = models.CharField(max_length=400, blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't1'