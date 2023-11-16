from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='home'),  # http://127.0.0.1:8000/
    path('', WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about
    path('addpage/', add_page, name='add_page'),  # http://127.0.0.1:8000/add_page
    path('contact/', contact, name='contact'),  # http://127.0.0.1:8000/contact
    path('login/', login, name='login'),  # http://127.0.0.1:8000/login

    # path('post/<int:post_id>/', show_post, name='post'),  # http://127.0.0.1:8000/post/post_id
    # path('post/<slug:post_slug>/', show_post, name='post'),  # http://127.0.0.1:8000/post/post_id
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),  # http://127.0.0.1:8000/post/post_id

    # path('category/<int:cat_id>/', show_category, name='category'),  # http://127.0.0.1:8000/post/post_id
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),  # http://127.0.0.1:8000/post/post_id

    # path('cats', categories),  # http://127.0.0.1:8000/cats
    # path('cat/<int:catid>/', category),  # http://127.0.0.1:8000/cat/1
    # path('cat-slug/<slug:cat>/', category_slug),  # http://127.0.0.1:8000/cat-slug/1
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/archive/2020/
    # re_path(r'^archive_redirect/(?P<year>[0-9]{4})/', archive_redirect),  # http://127.0.0.1:8000/archive_redirect/2020/
]

