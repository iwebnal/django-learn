from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения Women")


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def category(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям </h1><p>{catid}</p>")


def category_slug(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям (-- slug--) </h1><p>{cat}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам: </h1><p>{year}</p>")
