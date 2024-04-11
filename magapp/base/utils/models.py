from django.db import models


class LowerCharField(models.CharField):
    # Ensure valid values will always be using just lowercase
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return value if value is None else value.lower()
