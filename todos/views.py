from django.http import HttpResponse

def home(self):
    return HttpResponse("Home sweet home...")
