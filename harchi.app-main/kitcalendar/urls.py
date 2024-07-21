from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kitcalendar.views import DateConversionView, DateDifferenceView, AgeCalculatorView, TimezoneView, ReligiousTimeView


router = DefaultRouter()
router.register('date-conversion', DateConversionView, basename='date-conversion')
router.register('age-calculator', AgeCalculatorView, basename='age-calculator')
router.register('date-diff', DateDifferenceView, basename='date-diff')
router.register('current-time', TimezoneView, basename='current-time')
router.register('religous-times', ReligiousTimeView, basename='religous-times')
# router.register('calendar', DateConversionView, basename='calendar')

# print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    # path('sharia', DateDifferenceView, name='sharia'),
]
