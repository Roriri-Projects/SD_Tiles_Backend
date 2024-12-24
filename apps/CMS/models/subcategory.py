from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models
from apps.CMS.models import Category


class Subcategory(BaseModel):
    identity = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)

    def __str__(self):
        return f"{self.identity} {self.category.identity}"

    