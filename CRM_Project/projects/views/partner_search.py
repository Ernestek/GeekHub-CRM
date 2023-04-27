from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.permissions import TemporaryPasswordChanged
from partners.models import Partner
from projects.models import Project
from projects.serializers.pertner_search import PartnerSearchByCodeSerializer


@extend_schema(
    tags=('Project',),
    parameters=[
        OpenApiParameter(
            name='code',
            location='query',
            required=False,
            type=str,
        ),
    ],
    description='Search partner by code.'
)
class PartnerSearchByCodeView(APIView):
    serializer_class = PartnerSearchByCodeSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged)

    def get(self, request, format=None):
        query_code = self.request.query_params.get('code', None)
        if query_code:
            projects = Partner.objects.filter(code__contains=query_code)
            serializer = self.serializer_class(projects, many=True)
            return Response(serializer.data)
        else:
            return Response([])
