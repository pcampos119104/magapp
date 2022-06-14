import uuid

from slugify import slugify


def create_unique_slug(title):
    uuid_str = str(uuid.uuid4())
    return slugify(f"{title} {uuid_str[:8]}")
