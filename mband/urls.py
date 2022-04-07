from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

# schema_view = get_swagger_view(title='MBand API')

urlpatterns = [
    # path('auth', include('djoser.urls')),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', views.getRoutes),
    path('users', views.UserList.as_view()),
    path('profiles', views.ProfileList.as_view()),
    # path('profiles/test', views.ProfileSortList.as_view()),
    path('profile/update/<int:pk>', views.ProfileUpdateView.as_view()),
    path('profile/view', views.ProfileView.as_view()),
    path('profile/create', views.ProfileCreateView.as_view()),
    path('profile/image/upload', views.ImageUploadView.as_view()),
    path('register', views.CreateUserView.as_view()),
    path('skill/view', views.SkillView.as_view()),
    path('skill/create', views.SkillCreateView.as_view()),
    path('skill/delete/<int:pk>', views.GenreDeleteView.as_view()),
    path('genre/view', views.GenreView.as_view()),
    path('genre/create', views.GenreCreateView.as_view()),
    path('genre/delete/<int:pk>', views.GenreDeleteView.as_view()),
    path('subscription/create/<int:pk>', views.SubscriptionCreateView.as_view()),
    path('subscription/view', views.SubscriptionView.as_view()),
    path('subscription/delete/<int:pk>', views.SubscriptionDeleteView.as_view()),
    # path('link/create', views.CreateLinkYTView.as_view())
]
