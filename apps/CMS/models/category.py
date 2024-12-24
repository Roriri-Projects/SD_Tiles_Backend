from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models


class Category(BaseModel):
    identity = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)


    def __str__(self):
        return self.identity
    