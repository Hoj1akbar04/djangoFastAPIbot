import uuid
from django.db.models import TextChoices


class SaveMediaFile(object):
    def user_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'users/user//{uuid.uuid4()}.{image_extension}'

    def product_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'products/product//{uuid.uuid4()}.{image_extension}'

    def product_type_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'products/product_type//{uuid.uuid4()}.{image_extension}'

    def testimonial(self, filename):
        image_extension = filename.split('.')[-1]
        return f'users/testmonial//{uuid.uuid4()}.{image_extension}'


