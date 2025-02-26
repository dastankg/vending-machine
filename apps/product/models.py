from django.contrib.postgres.indexes import HashIndex
from django.core.validators import MinValueValidator
from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    count = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        indexes = (
            HashIndex(fields=('id',), name='uuid_hash_index'),
        )
