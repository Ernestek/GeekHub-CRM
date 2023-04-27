from rest_framework import serializers

from partners.models import Partner


class PartnerSearchByCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id',
            'code',
            'name',
        )
