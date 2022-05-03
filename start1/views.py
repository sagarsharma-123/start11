from django.http import HttpResponse

def indexv(request):
    return HttpResponse("hello")