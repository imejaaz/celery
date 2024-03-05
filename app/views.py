from django.http import HttpResponse
from django.shortcuts import render
from djangocelery.celery import check, testing
from .tasks import tes
from celery.result import AsyncResult
from time import sleep
def home(request):
    # return HttpResponse("this is good")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("this is good")
    result = testing.apply_async()
    print(result)
    return render(request, 'about.html', {'result' : result})

def contact(request):
    # return HttpResponse("this is good")
    tes.delay()
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse("this is good")
    return render(request, 'services.html')

def result(request, id):
    result = AsyncResult(id)
    print(result.id)
    print(result.task_id)
    print(result.state)
    print(result.status)
    print(result.result)

    return render(request, 'home.html', {'result': result})