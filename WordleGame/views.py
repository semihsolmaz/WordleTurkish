from django.shortcuts import render


def homePage(request):
    if request.method == 'POST':
        print(request.POST)


    return render(request, 'homePage.html')
