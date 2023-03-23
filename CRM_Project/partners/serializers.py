from rest_framework import serializers

from partners.models import Partner, PartnerContactPerson


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class PartnerContactPersonSerializer(serializers.ModelSerializer):
    partner_name = serializers.CharField(source='partner.name', allow_null=True)

    class Meta:
        model = PartnerContactPerson
        fields = '__all__'
