from rest_framework.routers import DefaultRouter
from .views import PersonalViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'personallists', PersonalViewset)

urlpatterns = [
    path('', include(router.urls))
]
