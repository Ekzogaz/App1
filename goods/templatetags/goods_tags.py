from atexit import register
from django import template
from goods.models import Categories
from django.utils.http import urlencode
from django.http import QueryDict

register = template.Library()


@register.simple_tag()

def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)

def change_params(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()



