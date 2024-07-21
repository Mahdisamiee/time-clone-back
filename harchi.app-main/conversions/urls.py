from django.urls import path, include
from rest_framework.routers import DefaultRouter
from conversions.views import TempConversion, GenericConversion


router = DefaultRouter()
router.register('temp-conv', TempConversion, basename='temp-conversion')
router.register('generic-conv', GenericConversion, basename='generic-conversions')

# print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
