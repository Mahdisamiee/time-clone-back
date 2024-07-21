from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kitmap.views import DistanceMatrixViewset, GetCitiesViewset


router = DefaultRouter()
router.register('dist-mat', DistanceMatrixViewset, basename='distance-matrix')
router.register('get-cities', GetCitiesViewset, basename='get-cities')

# print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
