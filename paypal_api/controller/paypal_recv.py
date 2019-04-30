
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views import View


import json

from Lib.PayPalApi import PayPalApi


class PaypalRecv(View):

    def get(self, request):

        paypayApi = PayPalApi();
        paypayApi.getOrder('2Y541645B36700718');

        return HttpResponse("aaa")

        pass;

    def post(self, request):
        reqBody = request.body;
        dataJson = (reqBody.decode('utf-8'));
        dataObj = json.loads(dataJson);

        orderID = dataObj.get("orderID");

        paypayApi = PayPalApi();
        orderInfo = paypayApi.getOrder( orderID );

        return JsonResponse(orderInfo);
        pass;
