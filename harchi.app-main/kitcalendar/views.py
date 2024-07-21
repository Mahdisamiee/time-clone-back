from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from kitcalendar.utils.date_diff import date_difference
from kitcalendar.utils.date_conversion_utils import jalali_to_gregorian, jalali_to_hijri, gregorian_to_hijri
from rest_framework.permissions import AllowAny 
from kitcalendar.models import NoneModel
from kitcalendar.utils.current_time import get_all_time_zones, get_current_time
from kitcalendar.utils.religous_times import get_prayer_times
from kitcalendar.utils.calendar import get_day_and_month_name

class DateDifferenceView(ViewSet):
    http_methods = ['post',]
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny] 
    
    @swagger_auto_schema(
        operational_description="this to get difference between two dates",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'date_type': openapi.Parameter(name='date_type', in_=openapi.IN_BODY,
                    description='date_type can be jalali hijri or gregorian',
                    type='string'),
                'start_year': openapi.Parameter(name='start_year', in_=openapi.IN_BODY,
                    description='start_year',
                    type='int'),
                'start_month': openapi.Parameter(name='start_month', in_=openapi.IN_BODY,
                    description='start_month',
                    type='int'),
                'start_day': openapi.Parameter(name='start_day', in_=openapi.IN_BODY,
                    description='start_day',
                    type='int'),
                'end_year': openapi.Parameter(name='end_year', in_=openapi.IN_BODY,
                    description='end_year',
                    type='int'),
                'end_month': openapi.Parameter(name='end_month', in_=openapi.IN_BODY,
                    description='end_month',
                    type='int'),
                'end_day': openapi.Parameter(name='end_day', in_=openapi.IN_BODY,
                    description='end_day',
                    type='int'),
            }
        ),
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                                {
                                    'year': years,
                                    'month': months,
                                    'day': days
                                }
                            """
                        )
                    }
                ),
            }
        )
    )
    def create(self, request):
        try:
            start_year = request.data.get('start_year')
            start_month = request.data.get('start_month')
            start_day = request.data.get('start_day')
            date_type = request.data.get('date_type')
            end_year = request.data.get('end_year')
            end_month = request.data.get('end_month')
            end_day = request.data.get('end_day')
            
            # TODO: convert to gregorian            
            if date_type == "hijri":
                start_date = str(gregorian_to_hijri(start_year, start_month, start_day, True))
                end_date = (gregorian_to_hijri(end_year, end_month, end_day, True))
            if date_type == "jalali":
                start_date = str(jalali_to_gregorian(start_year, start_month, start_day))
                end_date = str(jalali_to_gregorian(end_year, end_month, end_day))
            else:
                # Example usage:
                start_date = f"{start_year}-{start_month}-{start_day}"
                end_date = f"{end_year}-{end_month}-{end_day}"

            years, months, days = date_difference(start_date, end_date)
            print(f"Time difference: {years} years, {months} months, {days} days")
            return Response({
                'year': years,
                'month': months,
                'day': days
            })
        except:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AgeCalculatorView(ViewSet):
    http_methods = ['post',]
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny] 
    
    @swagger_auto_schema(
        operational_description="this to calculate age",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'date_type': openapi.Parameter(name='date_type', in_=openapi.IN_BODY,
                    description='date_type can be jalali hijri or gregorian',
                    type='string'),
                'start_year': openapi.Parameter(name='start_year', in_=openapi.IN_BODY,
                    description='start_year',
                    type='int'),
                'start_month': openapi.Parameter(name='start_month', in_=openapi.IN_BODY,
                    description='start_month',
                    type='int'),
                'start_day': openapi.Parameter(name='start_day', in_=openapi.IN_BODY,
                    description='start_day',
                    type='int'),
            }
        ),
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                                {
                                "years": 0,
                                "monthes": 0,
                                "days": 0,
                                "converted": {
                                    "year": {
                                    "hijri": 1445,
                                    "gregorian": 2024
                                    },
                                    "month": {
                                    "hijri": "رمضان",
                                    "gregorian": "march"
                                    },
                                    "day": {
                                    "hijri": 20,
                                    "gregorian": 1
                                    },
                                    "day_name": {
                                    "gregorian": "friday",
                                    "jalali": "جمعه",
                                    "hijri": "جمعه"
                                    }
                                }
                                }
                            """
                        )
                    }
                ),
            }
        )
    )
    def create(self, request):
        try:
            print(self.request.data)
            start_year = request.data.get('start_year')
            start_month = request.data.get('start_month')
            start_day = request.data.get('start_day')
            date_type = request.data.get('date_type')
            
            if date_type == "hijri":
                start_date = str(gregorian_to_hijri(start_year, start_month, start_day, True))
            elif date_type == "jalali":
                start_date = str(jalali_to_gregorian(start_year, start_month, start_day))
            else:
                start_date = f"{start_year}-{start_month}-{start_day}"
            end_date = str(datetime.now().date())
            print(start_date, end_date)
            yr, mr, dr, dnr = get_day_and_month_name(
                start_year, start_month, start_day, date_type
            )
            print(date_difference(start_date, end_date))
            years, months, days = date_difference(start_date, end_date)
            print(f"Time difference: {years} years, {months} months, {days} days")
            return Response({
                'years': years,
                'monthes': months,
                'days': days,
                'converted':{
                    'year': yr, 
                    'month': mr,
                    'day': dr,
                    'day_name': dnr
                }
            })
        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DateConversionView(ViewSet):
    http_methods = ['post',]
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny] 

    
    @swagger_auto_schema(
        operational_description="this to covert different date types to each other",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'conversiontype': openapi.Parameter(name='conversiontype', in_=openapi.IN_BODY,
                    description='conversion type which can be: j2h, h2j, j2g, g2j, g2h, h2g / j for jalali, g for gregorian and h for hijri',
                    type='string'),
                'year': openapi.Parameter(name='year', in_=openapi.IN_BODY,
                    description='year(to be converted)',
                    type='int'),
                'month': openapi.Parameter(name='month', in_=openapi.IN_BODY,
                    description='month(to be converted)',
                    type='int'),
                'day': openapi.Parameter(name='day', in_=openapi.IN_BODY,
                    description='day(to be converted)',
                    type='int'),
            }
        ),
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                            {
                                converted: "string-of-converted-date"
                            }
                            """
                        )
                    }
                ),
            }
        )
    )
    def create(self, request):
        try:
            year = request.data.get('year')
            month = request.data.get('month')
            day = request.data.get('day')
            conversion_type = request.data.get('conversiontype')
            result = ''
            if conversion_type == 'j2g':
                result = jalali_to_gregorian(year, month, day)
            elif conversion_type == 'g2j':
                result = jalali_to_gregorian(year, month, day, True)
            elif conversion_type == 'j2h':
                result = jalali_to_hijri(year, month, day)
            elif conversion_type == 'h2j':
                result = jalali_to_hijri(year, month, day, True)
            elif conversion_type == 'g2h':
                result = gregorian_to_hijri(year, month, day)
            elif conversion_type == 'h2g':
                result = gregorian_to_hijri(year, month, day, True)
        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({
            'converted': str(result)
        })


class TimezoneView(ViewSet):
    http_methods = ['get',]
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny] 

    
    @swagger_auto_schema(
        operational_description="getting all timezones",
        
        manual_parameters=[
            openapi.Parameter(name='timezone', in_=openapi.IN_QUERY,
                    description='',
                    type='string'),
        ],
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                            {
                                time: "string-of-current-time"
                            }
                            """
                        )
                    }
                ),
            }
        )
    )
    def list(self, request):
        try:
            timezone = request.query_params.get('timezone')
            print(request.query_params)
            if timezone is None:
                return Response({
                    'timezones': get_all_time_zones()
                })
            else:
                return Response({
                    'currenttime': get_current_time(timezone)
                })
        except:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReligiousTimeView(ViewSet):
    http_methods = ['get',]
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny] 

    
    @swagger_auto_schema(
        operational_description="getting all timezones",
        manual_parameters=[
            openapi.Parameter('latitude', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_NUMBER),
            openapi.Parameter('longitude', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_NUMBER),
            openapi.Parameter('year', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_INTEGER),
            openapi.Parameter('month', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_INTEGER),
            openapi.Parameter('day', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_INTEGER),
        ],
        # {
        #     'latitude': openapi.Parameter('latitude', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_NUMBER),
        #     'longitude': openapi.Parameter('longitude', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_NUMBER),
        #     'year': openapi.Parameter('year', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_INTEGER),
        #     'month': openapi.Parameter('month', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_INTEGER),
        #     'day': openapi.Parameter('day', openapi.IN_QUERY, description="Query parameter", type=openapi.TYPE_INTEGER),
        # }
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                            {
                                
                            }
                            """
                        )
                    }
                ),
            }
        )
    )
    def list(self, request):
        try:
            
            latitude = float(request.query_params.get('latitude'))
            longitude = float(request.query_params.get('longitude'))
            date_tuple = (
                int(request.query_params.get('year')), 
                int(request.query_params.get('month')), 
                int(request.query_params.get('day'))
            )

            prayer_times = get_prayer_times(latitude, longitude, date_tuple)

            # Print prayer times
            print("Fajr:", prayer_times['fajr'])
            print("Dhuhr:", prayer_times['dhuhr'])
            print("Asr:", prayer_times['asr'])
            print("Maghrib:", prayer_times['maghrib'])
            print("Isha:", prayer_times['isha'])
            
            return Response(prayer_times)

        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



