from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('cats', categories),  # http://127.0.0.1:8000/cats
    path('cat/<int:catid>/', category),  # http://127.0.0.1:8000/cat/1
    path('cat-slug/<slug:cat>/', category_slug),  # http://127.0.0.1:8000/cat-slug/1
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/archive/2020/
    re_path(r'^archive_redirect/(?P<year>[0-9]{4})/', archive_redirect),  # http://127.0.0.1:8000/archive_redirect/2020/
]
