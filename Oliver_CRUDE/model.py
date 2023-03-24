from django.db import models

class people(models.Model):
    name = models.CharField(max_length=30, blank=false, null=false)
    email = models.CharField(max_length=30, blank=false, null=false)
    age = models.IntegerField(max_length=30, blank=false, null=false)
    gender = models.CharField(max_length=30, blank=false, null=false)
    phone number = models.IntegerField(max_length=30, blank=false, null=false)
    amount = models.IntegerField(max_length=30, blank=false, null=false)


def __self__(self):
    return self.name