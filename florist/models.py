from django.db import models
import uuid


class Contact(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    still_actual = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_composition = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
