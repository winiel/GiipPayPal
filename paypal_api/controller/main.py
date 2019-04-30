
from django.http import HttpResponse
from django.template import loader
from django.views import View

class Main(View):

    def get(self, request):
        template = loader.get_template('main.html')
        context = {}
        return HttpResponse(template.render(context, request))

        pass;
