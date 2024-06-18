from django.contrib.auth.models import User
from django.db import models
from .helpers import SaveMediaFiles


class PriceType(models.TextChoices):
    EURO = 'EURO', 'EURO'
    DOLLAR = '$', '$'
    SUM = 'SO`M', 'SO`M'


class Product(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.product_image)
    name = models.CharField(max_length=25, null=True)
    slug = models.SlugField(unique=True, verbose_name='Slug', max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()
    price_type = models.CharField(max_length=4, choices=PriceType.choices)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        db_table = 'products'
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class Comment(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.clientcomment_image)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, verbose_name='Slug', max_length=100)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        db_table = 'comments'
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class Team(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.clientcomment_image)
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, verbose_name='Slug', max_length=100)
    staff_type = models.CharField(max_length=150)
    title = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        db_table = 'teams'
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.blog_image)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, verbose_name='Slug', max_length=100)
    who = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        db_table = 'blogs'
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    content = models.TextField()
    slug = models.SlugField(unique=True, verbose_name='Slug', max_length=100)
    image = models.ImageField(upload_to=SaveMediaFiles.testimonial)
    client_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class ProductsUsers(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=False)
    username = models.CharField(max_length=30, null=True, unique=True)
    telegram_id = models.PositiveBigIntegerField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products_users'


class ProductsProducts(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True)
    category_code = models.CharField(max_length=20)
    category_name = models.CharField(max_length=30)
    subcategory_code = models.CharField(max_length=20)
    subcategory_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'products_product'
