from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from kitcalendar.models import PersianCalendar
from kitcalendar.serializers import PCSerializer
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from kitcalendar.utils.date_conversion_utils import get_city_list, get_city_time_info, get_city_pray_table
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from kitcalendar.utils.date_conversion_utils import jalali_to_gregorian, jalali_to_hijri, gregorian_to_hijri


class PCViewSet(ReadOnlyModelViewSet):
    ''' example of quering:
    query this url http://127.0.0.1:8000/api/time-api/per-cal-events/?month=12
    to get all related events of esfand
    '''

    queryset = PersianCalendar.objects.all()
    serializer_class = PCSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = "__all__"


class GetCity(ViewSet):
    '''/api/time-api/get-city/
        you are only allowed to send get request to this url
        if you request in a list mode(without any url param) it will return the list of cities
        else if you set city code as url-param it returns the oughat sharie table and city info
    '''

    http_methods = ['get']
    queryset = PersianCalendar.objects.none()
        
    @swagger_auto_schema(
        operational_description="this to get distance between two places",
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'city lists': openapi.Schema(type=openapi.TYPE_OBJECT, name="distance", description="example result is"
                            """
                                {"Code":1,"Name":"تهران","LName":"Tehran","Type":"C","Country_Code":1,"Province_Code":0},
                            """
                        )
                    }
                ),
            }
        )
    )
    def list(self, request):
        return Response(
            get_city_list()
        )
        
    
    


    @swagger_auto_schema(
        operational_description="this to get distance between two places",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                type=openapi.TYPE_INTEGER,
                in_=openapi.IN_PATH,
                description="id of the city which has been choosed from get city list"
            )
        ],
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'city oughat sharie': openapi.Schema(type=openapi.TYPE_OBJECT, name="city info and oughat sharie", description="example result is"
                                '''
                                {
                                    "table": {some data},
                                    "info": {
                                        "CityName": "تهران",
                                        "CountryCode": "1",
                                        "CountryName": "ایران",
                                        "CityLName": "Tehran",
                                        "CountryLName": "Iran",
                                        "CountryAlpha2": "IR ",
                                        "TimeZone": "3.5",
                                        "Imsaak": "04:58:04",
                                        "Sunrise": "06:22:28",
                                        "SunriseDT": "10/28/2023 6:22:05 AM",
                                        "Noon": "11:48:12",
                                        "Sunset": "17:13:55",
                                        "Maghreb": "17:32:33",
                                        "Midnight": "23:06:00",
                                        "Today": "1402/8/6 - 2:06 PM",
                                        "TodayQamari": "1445/04/14",
                                        "TodayGregorian": null,
                                        "DayLenght": null,
                                        "SimultaneityOfKaaba": "13:57:00",
                                        "SimultaneityOfKaabaDesc": "زمان مقارنه خورشید و قبله:"
                                    }
                                }
                                    
                                '''
                        )
                    }
                ),
            }
        )
    )
    def retrieve(self, request, pk):
        ''' /api/time-api/get-city/ID/
            returns a json file like:
            {
                "table": get_city_pray_table(pk),
                "info":  get_city_time_info(pk)
            }
        '''
        return Response(
            {
                "table": get_city_pray_table(pk),
                "info":  get_city_time_info(pk)
            }
        )

