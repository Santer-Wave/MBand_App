from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CreateUserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']



class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SkillSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Skill
        fields = '__all__'


class CreateSkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}, 'skill': {'required': False}}


class GenreSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Genre
        fields = '__all__'


class CreateGenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}, 'genre': {'required': False}}


class ProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Avatar
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class ProfileSortSerializer(ModelSerializer):
    profiles = ProfileSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'profiles', 'skills', 'genres']


class SubscriptionListSerializer(ModelSerializer):
    profiles = ProfileSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'profiles', 'genres', 'skills']


class SubscriptionSerializer(ModelSerializer):
    subscribed = SubscriptionListSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}, 'subscribed': {'required': False}}