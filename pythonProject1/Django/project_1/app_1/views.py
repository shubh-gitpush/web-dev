from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    #return HttpResponse('hello world')
    dic={'insert_me':'hello i am in view'}
    return render(request,'new.html',context=dic)