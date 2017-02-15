from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(string, args):
    return string.split(args)


@register.filter
def multiply_add(_counter, _pagenum):
    return _counter, _pagenum


@register.filter
def one_more(_counter_pagenum, _totalpages):
    _counter, _pagenum = _counter_pagenum
    return _counter + (int(_totalpages[-1]) - _pagenum) * 10
