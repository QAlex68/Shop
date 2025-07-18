from django import template
from cart.models import Cart


register = template.Library() # регистрируем если хотим использовать


@register.simple_tag(takes_context=True)
# метод получения количества товара просто цифра
def get_cart_count(context):
    request = context['request']
    if not request.session.session_key:
        return 0

    try:
        cart = Cart.objects.get(session_key=request.session.session_key)
        return cart.total_items
    except Cart.DoesNotExist:
        return 0


@register.filter # фильтрация в наших шаблонах
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
