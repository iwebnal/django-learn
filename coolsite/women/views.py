from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# def index(request):
#     return HttpResponse("Страница приложения Women")


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def category(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям </h1><p>{catid}</p>")


def category_slug(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям (-- slug--) </h1><p>{cat}</p>")


def archive(request, year):
    if int(year) > 2020:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам: </h1><p>{year}</p>")


def archive_redirect(request, year):
    if int(year) > 2020:
        # return redirect('/')
        return redirect('home', permanent=True)  # home - women url name

    return HttpResponse(f"<h1>Архив по годам: </h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
