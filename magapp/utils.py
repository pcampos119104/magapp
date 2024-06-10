import uuid

from django.forms import forms
from slugify import slugify


def clean_unique(form, field, exclude_initial=True, format='O campo %(field) com valor %(value) já existe.'):
    """
    Check in the database if the field is unique.
    """
    value = form.cleaned_data.get(field)
    if value:
        qs = form._meta.model._default_manager.filter(**{field: value})
        if exclude_initial and form.initial:
            initial_value = form.initial.get(field)
            qs = qs.exclude(**{field: initial_value})
        if qs.count() > 0:
            raise forms.ValidationError(format % {'field': field, 'value': value})
    return value

def create_unique_slug(title):
    uuid_str = str(uuid.uuid4())
    return slugify(f"{title} {uuid_str[:8]}")