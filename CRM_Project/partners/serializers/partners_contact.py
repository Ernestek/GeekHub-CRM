from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from partners.models import PartnerContactPerson, Partner


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerContactPerson
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
        )


class ContactPersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerContactPerson
        fields = (
            'first_name',
            'last_name',
            'phone',
        )


class AddContactPersonToPartnerCard(serializers.ModelSerializer):
    partner_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PartnerContactPerson
        fields = (
            'id',
            'partner_id',
            'first_name',
            'last_name',
            'phone',
        )

    def validate(self, attrs):
        partner_id = attrs['partner_id']
        phone = attrs['phone']

        try:
            partner = Partner.objects.prefetch_related('contact_person').get(pk=partner_id)
        except (Partner.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'partner_id': _('Invalid partner id')},
                code='invalid_partner_id',
            )

        if phone in partner.contact_person.values_list('phone', flat=True):
            raise serializers.ValidationError(
                {'contact_phone': _('Contact with this number exists')},
                code='invalid_contact_phone',
            )
        return attrs


class RemoveFromPartnerContactsPersonSerializer(serializers.Serializer):
    partner_id = serializers.IntegerField(write_only=True)
    contact_id = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        partner_id = attrs['partner_id']
        contact_id = attrs['contact_id']

        try:
            partner = Partner.objects.prefetch_related('contact_person').get(pk=partner_id)
        except (Partner.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'partner_id': _('Invalid partner id')},
                code='invalid_partner_id',
            )

        if not (contact_id in partner.contact_person.values_list('id', flat=True)):
            raise serializers.ValidationError(
                {'contact_id': _('This contact is not on the contact person list')},
                code='invalid_contact_id',
            )
        attrs['partner'] = partner
        return attrs

    def create(self, validated_data):
        PartnerContactPerson.objects.get(pk=validated_data['contact_id']).delete()
        return validated_data['partner']
