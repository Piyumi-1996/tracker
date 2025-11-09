from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register, ActivityViewSet

router = DefaultRouter()
router.register('activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('auth/register/', register),                    # Register user
    path('auth/token/', TokenObtainPairView.as_view()),  # Login / get access token
    path('auth/token/refresh/', TokenRefreshView.as_view()),  # Refresh token
    path('', include(router.urls)),                      # Activity endpoints
]
