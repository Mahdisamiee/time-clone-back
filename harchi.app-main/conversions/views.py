from conversions.utils.conversions import *
from rest_framework.viewsets import ViewSet
from kitmap.models import NoneModel
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status



class GenericConversion(ViewSet):
    http_methods = ['post', 'get']
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny]


    def list(slef, request):
        
        return Response({
            'generic': get_generics()
        })

    def retrieve(self, request, pk=None):
        
        return Response({
            'units': get_pu_for_unit(pk)
        })
    
    @swagger_auto_schema(
        operational_description="this to get distance between two places",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'unit': openapi.Parameter(name='unit', in_=openapi.IN_BODY,
                    description='this is the generic mode of conversion can be length, area and etc which you can get the list of that from get urls',
                    type='string'),
                'from_unit': openapi.Parameter(name='from_unit', in_=openapi.IN_BODY,
                    description='sub unit of the generic mode which you have to get the modes from get urls',
                    type='string'),
                'to_unit': openapi.Parameter(name='to_unit', in_=openapi.IN_BODY,
                    description='the value will be converted to this unit',
                    type='string'),
                'val': openapi.Parameter(name='val', in_=openapi.IN_BODY,
                    description='this is the value of the input that gonna be converted',
                    type='float'),
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
                                result: "error message here"
                            }
                            
                            OR
                            
                            {
                                result: 123
                            }
                            """
                        )
                    }
                ),
            }
        )
    )
    def create(self, request):
        res = unit_conv(
            request.data['unit'],
            request.data['from_unit'],
            request.data['to_unit'],
            request.data['val']
        )
        if request.data['unit'] not in ('data-transfer', 
            'digital-storage') or float('%.3f'%(res)) != 0:
            res = float('%.3f'%(res))
        return Response(
            {
                'result': res
            }
        )



class TempConversion(ViewSet):
    http_methods = ['post', 'get']
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny]
    
    
    def list(self, request):
        return Response(
            {
                'modes': temp_conversion_modes()
            }
        )

    @swagger_auto_schema(
        operational_description="this is for convertnig different temperature units to each other",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'conv_mode': openapi.Parameter(name='conv_mode', in_=openapi.IN_BODY,
                    description='this is the conversion mode that should have a specific mode FROM2TO',
                    type='string'),
                'val': openapi.Parameter(name='val', in_=openapi.IN_BODY,
                    description='this is the value of input which gonna be converted',
                    type='float'),
            }

        ),
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="this can be a string of error message or decimal value of response"
                            """
                            {
                                result: "error message here"
                            }
                            
                            OR
                            
                            {
                                result: 125
                            }
                            
                            """
                        )
                    }
                ),
            }
        )
    )
    def create(self, request):
        res = temp_conversion(
            request.data['conv_mode'],
            request.data['val']
        )
        res = float('%.3f'%(float(res)))
        return Response(
            {
                'result': res
            }
        )
