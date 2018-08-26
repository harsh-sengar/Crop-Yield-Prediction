from django.http import HttpResponse
from django.template import loader
#from .models import Album

def index(request):
    template=loader.get_template('frontpage/index.html')
    context={
     'all':'ahiadh'
    }
    return HttpResponse(template.render(context,request))

    #return HttpResponse()
