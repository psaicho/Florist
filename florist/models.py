from django.db import models
import uuid

class Contact_Model(models.Model):
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

