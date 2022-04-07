from rest_framework import permissions, generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view
from django.urls import path
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework_swagger.views import get_swagger_view


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/profiles',
            'method': 'GET',
            'body': None,
            'description': 'Возвращает список пользователей'
        }
    ]
    return Response(routes)


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CreateUserView(CreateAPIView):
    model = User
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


# class ProfileList(generics.ListAPIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = Profile.objects.all()
#         user = self.request.user
#         params = self.request.query_params
#
#         status_type = params.get('status', None)
#
#         if status_type:
#             queryset = queryset.filter(status=status_type)
#         if user.is_authenticated:
#             return queryset
#         raise PermissionDenied()


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSortSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = User.objects.all()
        params = self.request.query_params
        genre = params.get('genre', None)
        skill = params.get('skill', None)

        if genre:
            queryset = queryset.filter(genres__genre=genre)
        if skill:
            queryset = queryset.filter(skills__skill=skill)
        return queryset


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            profile = Profile.objects.filter(user=user)
            return profile
        raise PermissionDenied()


class ProfileCreateView(CreateAPIView):
    model = Profile
    serializer_class = CreateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        profile = Profile(user=self.request.user)
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.ListAPIView):
    serializer_class = ProfileSortSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return User.objects.filter(id=user.id)
        raise PermissionDenied()


class SkillView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Skill.objects.filter(user=user)
        raise PermissionDenied()


class SkillCreateView(CreateAPIView):
    model = Skill
    serializer_class = CreateSkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        skill = Skill(user=self.request.user)
        serializer = self.serializer_class(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillDeleteView(APIView):
    model = Skill
    serializer_class = SkillSerializer
    permission_classes = (IsUser,)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        skill = get_object_or_404(Skill, pk=pk)
        if skill.user == self.request.user:
            skill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise PermissionDenied()


class GenreView(generics.ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Genre.objects.filter(user=user)
        raise PermissionDenied()


class GenreCreateView(CreateAPIView):
    model = Genre
    serializer_class = CreateGenreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        genre = Genre(user=self.request.user)
        serializer = self.serializer_class(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDeleteView(APIView):
    model = Genre
    serializer_class = GenreSerializer
    permission_classes = (IsUser,)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        genre = get_object_or_404(Genre, pk=pk)
        if genre.user == self.request.user:
            genre.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise PermissionDenied()


class SubscriptionDeleteView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsUser,)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        subscription = get_object_or_404(Subscription, pk=pk)
        if subscription.user == self.request.user:
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise PermissionDenied()



class SubscriptionCreateView(CreateAPIView):
    model = Subscription
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = User.objects.get(id=pk)
        subscription = Subscription(user=self.request.user, subscribed=user)
        serializer = self.serializer_class(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Subscription.objects.all()
        user = self.request.user

        if user.is_authenticated:
            return queryset.filter(user=user.id)


class ImageUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        user = self.request.user
        serializer = ImageSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
