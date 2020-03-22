from django.db import models
from django.utils import timezone
from hashlib import sha256
import pickle

# Create your models here.

def create_friendly_name(province, region):
    return str(province) + ' - ' + str(region) if str(province) is not '' else str(region)


def create_hash(friendly_name):
    return sha256(friendly_name.encode()).hexdigest()


class CaseStatusType(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return str(self.name)


class Location(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    province_state = models.CharField(max_length=100, default='')
    region_country = models.CharField(max_length=100, default='')
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    friendly_name = create_friendly_name(province_state, region_country)
    friendly_hash = models.CharField(default=create_hash(friendly_name), max_length=100)
    def __str__(self):
        return self.friendly_name


class HistoricEntry(models.Model):
    date = models.DateField()
    count = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    case_status_type_id = models.ForeignKey(CaseStatusType, on_delete=models.DO_NOTHING)
    def __str__(self):
       return str(self.date) + ':' + str(self.count)