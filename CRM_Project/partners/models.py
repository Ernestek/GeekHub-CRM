from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel
from common.validators import validate_name, partner_code_validator


class Partner(BaseModel):
    name = models.CharField(max_length=255,)
    code = models.CharField(max_length=10, unique=True, validators=[partner_code_validator])

    def __str__(self):
        return f'{self.name} (code: {self.code})'
    

class PartnerContactPerson(BaseModel):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, related_name='contact_person')
    first_name = models.CharField(_('first name'), max_length=150, validators=[validate_name])
    last_name = models.CharField(_('last name'), max_length=150, validators=[validate_name])
    phone = PhoneNumberField()
    # phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'id: {self.id}, {self.first_name} {self.last_name}'

