from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def combine_arg(value, arg):
    return f"{value} {arg}"

register.filter("combarg", combine_arg)
