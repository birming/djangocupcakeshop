from django import template

register = template.Library()

@register.filter
def get_range2(value):
    """
     Filter - returns a list containing range made from given value
     Usage (in template):
    """
    return range(int(value))