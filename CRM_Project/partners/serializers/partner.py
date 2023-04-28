from rest_framework import serializers

from partners.models import Partner, PartnerContactPerson
from partners.serializers.partners_contact import ContactPersonSerializer
from projects.serializers.project import ProjectListSerializer


class PartnerSerializer(serializers.ModelSerializer):
    contact_person = ContactPersonSerializer(many=True)

    class Meta:
        model = Partner
        fields = (
            'id',
            'name',
            'code',
            'contact_person',
        )

    def validate(self, attrs):
        contact_person = attrs['contact_person']

        phone_list = []
        for contact in contact_person:
            phone_list.append(contact.get('phone'))

        if len(phone_list) > len(set(phone_list)):
            raise serializers.ValidationError(
                {'contact_person': 'Duplicate contact numbers'},
                code='invalid_partner_id',
            )

        return attrs

    def create(self, validated_data):
        contact_person_data = validated_data.pop('contact_person')
        partner = Partner.objects.create(**validated_data)
        for person_data in contact_person_data:
            PartnerContactPerson.objects.create(partner=partner, **person_data)
        return partner


class PartnerListSerializer(serializers.ModelSerializer):
    contact_person = ContactPersonSerializer(many=True)

    class Meta:
        model = Partner
        fields = (
            'id',
            'name',
            'contact_person',
        )


class PartnerRetrieveSerializer(serializers.ModelSerializer):
    contact_person = ContactPersonSerializer(many=True)
    project = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Partner
        fields = (
            'name',
            'code',
            'contact_person',
            'project',
        )
