from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
