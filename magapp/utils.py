import uuid

from django.forms import forms
from slugify import slugify


def clean_unique(form, field, exclude_initial=True, format='O campo %(field) com valor %(value) já existe.'):
    """Valida se o valor de um campo do formulário é único no banco de dados.

    Parâmetros:
        form: Instância de formulário contendo cleaned_data e metadados do modelo.
        field (str): Nome do campo a ser validado.
        exclude_initial (bool): Quando True, desconsidera o valor inicial do campo (útil em edições).
        format (str): Mensagem de erro com placeholders %(field) e %(value).

    Retorna:
        Any: O valor validado do campo.

    Lança:
        forms.ValidationError: Se já existir um registro com o mesmo valor para o campo.
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
    """Gera um slug único a partir de um título, anexando um sufixo UUID curto.

    Parâmetros:
        title (str): Texto base para a criação do slug.

    Retorna:
        str: Slug em formato URL-safe com sufixo de 8 caracteres do UUID.
    """
    uuid_str = str(uuid.uuid4())
    return slugify(f'{title} {uuid_str[:8]}')
