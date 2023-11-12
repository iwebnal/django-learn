from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
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
    # cats = Category.objects.all()
    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
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


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)  # get post by id from DB. get_object_or_404 - Django method

    # dictionary for post.html template
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)


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
