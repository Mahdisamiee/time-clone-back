from rest_framework.viewsets import ViewSet
from conversions.utils.conversions import temp_conversion
from kitmap.models import NoneModel
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from kitmap.utils import distance_matrix
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from kitmap.utils import feed_cities_in_iran


class DistanceMatrixViewset(ViewSet):
    '''getting the distance between origin and destination
    '''


    http_methods = ['post']
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny]


    @swagger_auto_schema(
        operational_description="this to get distance between two places",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'origin_lat': openapi.Parameter(name='origin_lat', in_=openapi.IN_BODY,
                    description='this is the origin and source latitude',
                    type='float'),
                'origin_lon': openapi.Parameter(name='origin_lon', in_=openapi.IN_BODY,
                    description='this is the origin and source longtitude',
                    type='float'),
                'dest_lat': openapi.Parameter(name='dest_lat', in_=openapi.IN_BODY,
                    description='this is the destination latitude',
                    type='float'),
                'dest_lon': openapi.Parameter(name='dest_lon', in_=openapi.IN_BODY,
                    description='this is the destination longtitude',
                    type='float'),
            }

        ),
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'distance': openapi.Schema(type=openapi.TYPE_OBJECT, name="distance", description="example result is"
                            """
                            {
                                "distance": [
                                    {
                                    "origin_index": "b",
                                    "destination_index": "c",
                                    "distance": 442687.7
                                    }
                                ],
                                "duration": [
                                    {
                                    "origin_index": "b",
                                    "destination_index": "c",
                                    "duration": 17787.3
                                    }
                                ],
                                "origins": {
                                    "b": {
                                    "name": "سایه",
                                    "province_name": "تهران",
                                    "county_name": "تهران",
                                    "district_title": "تهران",
                                    "ruraldistrict_title": "شهر تهران",
                                    "suburb_title": "منطقه ۵ شهر تهران",
                                    "neighbourhood_title": "محله فردوس"
                                    }
                                },
                                "destinations": {
                                    "c": {
                                    "name": "آذر",
                                    "province_name": "اصفهان",
                                    "county_name": "اصفهان",
                                    "district_title": "اصفهان",
                                    "ruraldistrict_title": "اصفهان",
                                    "suburb_title": "منطقه ۱",
                                    "neighbourhood_title": "محله عباس آباد"
                                    }
                                }
                            }
                            """
                        )
                    }
                ),
                # status.HTTP_201_CREATED: openapi.Schema(
                #     type=openapi.TYPE_OBJECT,
                #     properties={
                #     'students': openapi.Schema(type=openapi.TYPE_OBJECT)
                #     }
                # ),
            }
        )
    )
    def create(self, request):

        return Response(
            distance_matrix(
                origin_lat=request.data['origin_lat'],
                origin_lon=request.data['origin_lon'],
                dest_lat=request.data['dest_lat'],
                dest_lon=request.data['dest_lon']
            )
        )


class GetCitiesViewset(ViewSet):
    http_methods = ['get',]
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny] 

    
    @swagger_auto_schema(
        operational_description="getting list of all cities based on country",        
        manual_parameters=[
            openapi.Parameter(name='country_name', in_=openapi.IN_QUERY,
                    description='this is the country name that you wanna get its cities info',
                    type='string'),
        ],
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                            [
                                {
                                    'name': string
                                    'longitude': int,
                                    'latitude': int,
                                },
                                ...
                            ]
                            """
                        )
                    }
                ),
            }
        )
    )
    def list(self, request):
        try:
            country_name = request.query_params.get('country_name')
            # print(request.query_params)
            # TODO: Later this will change
            temp_res = feed_cities_in_iran()
            print(temp_res)
            if country_name is None:
                return Response(temp_res)
            elif country_name.lower() == "iran":
                return Response(temp_res)
            else:
                return Response({
                    'msg': "selected country is not supported yet"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

