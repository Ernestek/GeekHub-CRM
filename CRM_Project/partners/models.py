from django.db import models
from common.models import BaseModel


class Partner(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    

class PartnerContactPerson(BaseModel):
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
