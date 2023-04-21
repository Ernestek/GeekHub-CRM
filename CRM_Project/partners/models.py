from django.db import models
from common.models import BaseModel

from phonenumber_field.modelfields import PhoneNumberField


class Partner(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.name} (code: {self.code}) | Add: {self.address}'
    

class PartnerContactPerson(BaseModel):
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    # phone = models.CharField(max_length=10, blank=True, null=True, unique=True)
    phone = PhoneNumberField(null=True, blank=False, unique=True)

    def __str__(self):
        return f'{self.name} | {self.phone} | {self.email} | Company: {self.partner.name}'

