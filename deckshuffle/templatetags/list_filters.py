from django import template
register = template.Library()
@register.filter
def first(list):
    if list is not None and len(list):
        return list[0]

