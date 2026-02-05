# Django Imports
from django.db import models
import uuid

class TimeStampedModel(models.Model):
    """
    An abstract base class that provides self-updating
    'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    An abstract base class that uses UUID as the primary key.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True
    )
    
    class Meta:
        abstract = True


class AppBaseModel(TimeStampedModel, UUIDModel):
    """
    The standard base model for most entities.
    Combines UUID primary key with timestamps.
    """
    class Meta: # type: ignore
        abstract = True