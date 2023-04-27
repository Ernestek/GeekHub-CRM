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

    def create(self, validated_data):
        contact_person_data = validated_data.pop('contact_person')
        partner = Partner.objects.create(**validated_data)
        # for person_data in contact_person_data:
        #     person, created = PartnerContactPerson.objects.get_or_create(phone=person_data['phone'],
        #                                                                  defaults=person_data)
        #
        # return partner

        contact_persons_to_create = []
        for cp_data in contact_person_data:
            phone_number = cp_data.pop('phone')
            contact_person, created = PartnerContactPerson.objects.update_or_create(phone=phone_number, defaults=cp_data)
            partner.contact_person.add(contact_person)

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
