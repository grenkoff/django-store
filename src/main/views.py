from django.http import HttpResponse
from django.shortcuts import render


# это не функции, это представления или контролеры
# представления нужно закрепить за каким-либо url-адресом в файле urls.py
def index(request):
    # имитация базы данных
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    # return HttpResponse('Home page')
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')