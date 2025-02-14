from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

# Set up router
router = DefaultRouter()
router.register(r'patients', PatientViewSet)

# Include the router URLs
urlpatterns = [
    path('api/', include(router.urls)),
]
