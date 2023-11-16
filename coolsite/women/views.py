from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import *
from .models import *

# def index(request):
#     return HttpResponse("Страница приложения Women")


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


class WomenHome(ListView):
    model = Women  # selects all records from the table and displays them as a list
    template_name = 'women/index.html'
    context_object_name = 'posts'

    # extra_context = {'title': 'Главная страница'}  # extra_context - for static content data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0

        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)  # to display published posts


# def index(request):
#     posts = Women.objects.all()
#     # cats = Category.objects.all()
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#     return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')  # to force redirect to home page
    # reverse_lazy - better to use than reverse

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'

        return context


# def add_page(request):
#     # form = AddPostForm()
#
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # save data from Form
#             return redirect('home')
#
#             # try:
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#
#             # print(form.cleaned_data)
#     else:
#         form = AddPostForm()
#
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse("<h1>Авторизация</h1>")


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def category(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям </h1><p>{catid}</p>")


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    # pk_url_kwarg = 'post_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['cat_selected'] = context['post'].cat_id

        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)  # get post by id from DB. get_object_or_404 - Django method
#
#     # dictionary for post.html template
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#     return render(request, 'women/post.html', context=context)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # for generate 404 error, if 'False'

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                    is_published=True)
        # 'cat_slug' - comes from URL data
        # 'cat__slug' - access the slug field of the category table

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id

        return context


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     # cats = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404
#
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id
#     }
#     return render(request, 'women/index.html', context=context)


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
