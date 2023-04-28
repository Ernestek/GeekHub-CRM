from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from account.serializers.profile import UserRetrieveSerializer, UserUpdateSerializer, \
    SetProfileImageSerializer
from common.permissions import TemporaryPasswordChanged

User = get_user_model()


@extend_schema(
    tags=['Account'],
    description='User profile data'
)
class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged]

    def get_object(self):
        return self.request.user


@extend_schema(
    tags=['Account'],
    description='Update user profile data'
)
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged]

    def get_object(self):
        return self.request.user


# @extend_schema(
#     tags=['Account'],
#     request=SetProfileImageSerializer,
#     description='Update user profile image'
# )
# class ProfileImageUpdateView(CreateAPIView):
#     serializer_class = SetProfileImageSerializer
#     permission_classes = [AllowAny]
#     parser_classes = (FormParser, MultiPartParser)
#     authentication_classes = [TokenAuthentication]