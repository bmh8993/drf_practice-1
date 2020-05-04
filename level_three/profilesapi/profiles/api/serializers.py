from rest_framework import serializers
from ..models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)
    # user와 avatar를 따로 선언하지 않았을 때에 결과물은?

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvartarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"
