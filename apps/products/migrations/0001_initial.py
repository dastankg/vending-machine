# Generated by Django 5.1.6 on 2025-02-27 04:25

import django.contrib.postgres.indexes
import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Count')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'indexes': [django.contrib.postgres.indexes.HashIndex(fields=['id'], name='uuid_hash_index')],
            },
        ),
    ]
