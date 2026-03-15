from django import template

register = template.Library()


@register.filter
def delay_class(counter):
    """Return reveal-delay-N class based on loop counter (1-indexed)."""
    n = ((counter - 1) % 5) + 1
    return f'reveal-delay-{n}'
