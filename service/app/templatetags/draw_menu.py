from django import template
from django.db.models import QuerySet, Q

from app.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(title: str | None = None) -> QuerySet:
    if title:
        return Menu.objects.prefetch_related("child").filter(parent__title=title)
    return Menu.objects.filter(parent=None).prefetch_related("child")
