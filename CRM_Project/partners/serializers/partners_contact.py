from rest_framework import serializers

from partners.models import PartnerContactPerson


class ContactPersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerContactPerson
        fields = (
            'first_name',
            'last_name',
            'phone',
        )
