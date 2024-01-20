from django.http import HttpResponse
from django.shortcuts import render


# это не функции, это представления или контролеры
# представления нужно закрепить за каким-либо url-адресом в файле urls.py
def index(request):
    # имитация базы данных
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    # return HttpResponse('Home page')
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный'
    }

    # return HttpResponse('Home page')
    return render(request, 'main/about.html', context)
