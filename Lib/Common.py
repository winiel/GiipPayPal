from django.http import JsonResponse

class Common(object)   :
    def response(self, result, message, data):
        reVal = {
            "result"    : result,
            "message"   : message,
            "data"      : data
        };
        print(str(reVal));
        return JsonResponse(reVal);

