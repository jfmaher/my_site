from django.http import HttpResponse

def index(request):
    return HttpResponse(b'Hello django world!!')
