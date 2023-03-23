from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from partners.models import Partner, PartnerContactPerson
from partners.serializers import PartnerSerializer, PartnerContactPersonSerializer


class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PartnerSerializer


class PartnerContactPersonViewSet(ModelViewSet):
    queryset = PartnerContactPerson.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PartnerContactPersonSerializer
