from django.urls import path, include
from rest_framework.routers import DefaultRouter
from currencies.views import OnlineCurrencyMonitoring


router = DefaultRouter()
router.register('online-currencies', OnlineCurrencyMonitoring, basename='online-currencies')

# print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
