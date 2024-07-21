from conversions.utils.conversions import *
from rest_framework.viewsets import ViewSet
from kitmap.models import NoneModel
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from currencies.utils.currencies import get_currencies_online


class OnlineCurrencyMonitoring(ViewSet):
    http_methods = ['get']
    queryset = NoneModel.objects.none()
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operational_description="this is to get online price of different currencies",
        responses=openapi.Responses(
            responses={
                status.HTTP_200_OK: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                    'result': openapi.Schema(type=openapi.TYPE_OBJECT, name="result", description="example result is"
                            """
                                [
                                    {'item': 'بورس', 'price': '2,153,955', 'rate': '(0%)'},
                                    {'item': 'انس طلا', 'price': '2,032.92', 'rate': '(0.31%)'},
                                    {'item': 'مثقال طلا', 'price': '111,160,000', 'rate': '(0%)'},
                                    {'item': 'طلا ۱۸', 'price': '25,658,000', 'rate': '(0%)'},
                                    {'item': 'سکه', 'price': '302,950,000', 'rate': '(0%)'},
                                    {'item': 'دلار', 'price': '509,200', 'rate': '(0%)'},
                                    {'item': 'یورو', 'price': '559,090', 'rate': '(0%)'},
                                    {'item': 'نفت برنت', 'price': '76.29', 'rate': '(0.09%)'},
                                    {'item': 'بیت کوین', 'price': '46771.46', 'rate': '(0.36%)'}
                                ]
                            """
                        )
                    }
                ),
            }
        )
    )
    def list(slef, request):
        return Response(get_currencies_online())


    def retrieve(self, request, pk=None):
        tmp = get_currencies_online()
        items = tmp['currencies']
        date = tmp['date']
        time = tmp['time']
        to_ret = {}
        print(5*'#' + str(pk).strip())
        for item in items:
            print(5*'$' + item['item'])
            if item['item'] == str(pk).strip():
                to_ret = item
                break
        to_ret['date'] = date
        to_ret['time'] = time
        return Response(to_ret)
