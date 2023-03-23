from rest_framework import serializers

from partners.models import Partner, PartnerContactPerson


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class PartnerContactPersonSerializer(serializers.Serializer):
    class Meta:
        model = PartnerContactPerson
        fields = '__all__'
