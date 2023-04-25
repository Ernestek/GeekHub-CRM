from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from common.permissions import TemporaryPasswordChanged, IsStaff
from partners.models import Partner
from partners.serializers.partner import PartnerSerializer, PartnerListSerializer, PartnerRetrieveSerializer


@extend_schema(
    tags=('Partners',),
    description='',
)
class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.prefetch_related('contact_person')
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsStaff)
    serializer_class = PartnerSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related('project', 'project__owner')

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PartnerListSerializer
        elif self.action == 'retrieve':
            return PartnerRetrieveSerializer
        return PartnerSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff]
        else:
            permission_classes = [IsAuthenticated, TemporaryPasswordChanged]
        return [permission() for permission in permission_classes]
