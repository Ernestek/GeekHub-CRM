from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.fields import ImageField

User = get_user_model()


class UserRetrieveSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
            'profile_image',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=None, default=False)
    # last_name = serializers.CharField(max_length=None, required=False)
    # phone_number = serializers.CharField(max_length=None, required=False)
    # phone_number2 = serializers.CharField(max_length=None, required=False)
    # phone_number3 = serializers.CharField(max_length=None, required=False)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
        )


    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     profile_data = request.data.pop('profile', {})
    #     profile_serializer = ProfileSerializer(instance=instance.profile, data=profile_data, partial=True)
    #     profile_serializer.is_valid(raise_exception=True)
    #     self.perform_update(profile_serializer)
    #
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     return Response(serializer.data)
    #
    # def perform_update(self, serializer):
    #     serializer.save()

class SetProfileImageSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(max_length=None, required=False)
    # id = serializers.IntegerField()
    class Meta:
        model = User
        fields = ('profile_image',)

    # def create(self, validated_data):
    #     img = validated_data['profile_image']
    #     pid = validated_data['id']
    #     user = User.objects.get(pk=pid)
    #     user.profile_image = img
    #     user.save()
    #     return img
    def create(self, validated_data):
        img = validated_data['profile_image']
        self.user.profile_image = img
        self.user.save()
        return img
    # @extend_schema_field({'type': "string", 'format': 'binary',
    #                       'example': {
    #                           "profile_image": {"url": "string", "name": "string"},
    #                           "thumbnail": {"url": "string", "name": "string"}
    #                       }
    #                       })
    # def get_profile_image(self):
    #     return


# @extend_schema_field(OpenApiTypes.BINARY)
# class PictureSerializerField(serializers.ModelSerializer):
#     profile_image = ImageField(max_length=None, required=False)
#
#     class Meta:
#         model = User
#         fields = ('profile_image',)

    # def post_profile_image(self):
    #     return
@extend_schema_field(OpenApiTypes.BINARY)
class PictureSerializerField(serializers.ImageField):
    ...

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)