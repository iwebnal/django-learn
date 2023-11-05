from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

# def index(request):
#     return HttpResponse("Страница приложения Women")


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(request):
    return HttpResponse("<h1>Добавление статьи</h1>")


def contact(request):
    return HttpResponse("<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse("<h1>Авторизация</h1>")


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def category(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям </h1><p>{catid}</p>")


def show_post(request, post_id):
    return HttpResponse(f"<h1>Отображение статьи с id: </h1><p>{post_id}</p>")


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
