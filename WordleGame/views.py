import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def homePage(request):
    if request.method == 'POST':
        pass
    # print(request.POST)

    return render(request, 'homePage.html')


@csrf_exempt
def play(request):
    if request.method == 'POST' and request.is_ajax():
        cell = request.POST.get('c11')
        print(request.POST)
        print(cell)
        return HttpResponse(json.dumps({'cell': 'cellVal'}), content_type="application/json")  # Sending a success response
    else:
        return HttpResponse("Request method is not a GET")
