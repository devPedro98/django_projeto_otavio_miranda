from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Pedro Santos Barrios'
    })
    #return HTTP response


