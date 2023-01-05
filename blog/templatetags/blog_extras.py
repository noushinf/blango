from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()
user_model = get_user_model()


@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""
    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
    else:
        name = escape(f"{author.username}")
    if author.email:
        # email = escape(author.email)
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")

    else:
        prefix = ""
        suffix = ""
    # return mark_safe(f"{prefix}{name}{suffix}")
    return format_html('{}{}{}', prefix, name, suffix)
