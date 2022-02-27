from django import template

register = template.Library()


def stars(value):
    stars = int(value)
    return "⭐" * stars
