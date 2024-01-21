from django.shortcuts import render

from goods.models import Categories

# это не функции, это представления или контролеры
# представления нужно закрепить за каким-либо url-адресом в файле urls.py
def index(request):

    categories = Categories.objects.all()
    # имитация базы данных
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
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
