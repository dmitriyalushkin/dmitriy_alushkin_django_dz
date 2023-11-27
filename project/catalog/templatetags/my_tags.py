from django import template

from django.db.models.fields.files import FieldFile

register = template.Library()

@register.simple_tag
@register.filter()
def mediapath(data: FieldFile) -> str:
    """
    Make url path to media

    Examples:
        <img src="{{ object.image|mediapath }}" />
        or
        <img src="{% mediapath object.image %}" />
    """
    return data.url if data else '#'