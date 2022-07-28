from django import template
from djmoney.money import Money
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i-1]

@register.filter
def isequal(value, i):
    return value==i


@register.filter
def index2(indexable, i):
    # print(indexable[i],indexable[i-1],indexable[i-2],indexable[i-3])
    return indexable[i-2]

@register.filter
def curr(val="INR"):
    # print(val)
    c=str(Money(4.5,val))[0]
    # print(c)
    return c



@register.simple_tag
def define(val=None):
    return val
