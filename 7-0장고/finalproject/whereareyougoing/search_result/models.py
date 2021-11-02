from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    upjong = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    rat_count = models.IntegerField(blank=True, null=True)
    rat_avg = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Tourspots(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    keyword = models.CharField(max_length=45, blank=True, null=True)
    content = models.CharField(max_length=250, blank=True, null=True)
    tag = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    address1 = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourspots'
