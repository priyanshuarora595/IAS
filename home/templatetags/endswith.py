from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=False)
@stringfilter
def endswith(value, suffix):
    return str(value).endswith(suffix)