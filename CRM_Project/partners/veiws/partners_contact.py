from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status, mixins
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from common.permissions import TemporaryPasswordChanged, IsStaff
from partners.models import PartnerContactPerson
from partners.serializers.partners_contact import RemoveFromPartnerContactsPersonSerializer, \
    ContactPersonUpdateSerializer
from partners.serializers.partners_contact import AddContactPersonToPartnerCard


@extend_schema(
    tags=('Partners',),
    description='Add partner contacts',
    responses={
        204: OpenApiResponse(description='Contact added.'),
    }
)
class AddUserInPartnerContacts(CreateAPIView):
    serializer_class = AddContactPersonToPartnerCard
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    tags=('Partners',),
    description='Remove partner contacts',
    responses={
        204: OpenApiResponse(description='Contact person removed.'),
    }
)
class DeleteUserFromPartnerContacts(GenericAPIView):
    serializer_class = RemoveFromPartnerContactsPersonSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsStaff)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    tags=('Partners',),
    description='Edit partner contact',
)
class ContactPersonUpdateViewSet(mixins.UpdateModelMixin,
                                 GenericViewSet):
    queryset = PartnerContactPerson.objects
    serializer_class = ContactPersonUpdateSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsStaff)
