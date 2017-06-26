from django import template

register = template.Library()


@register.filter(name='choice_value')
def choice_value(form, key):
    return dict(form.fields['choices'].choices)[key]
