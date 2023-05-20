from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<marquee><h1>Srujana Tinnava Ra,Yera Vadilestunava...!</h1></marquee>')
def revi(request):
    return HttpResponse('<marquee><b>Mama Kutty,Long Drive Polamaaa...!</b></marquee>')