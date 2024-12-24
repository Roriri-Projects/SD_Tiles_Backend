from apps.BASE.model_fields import SingleFileField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models
from apps.CMS.models import Category,Subcategory




class ProductImage(BaseModel):
    file =SingleFileField(upload_to="product/images/")
class Product(BaseModel):
    identity = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    barcode = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    piece_rate = models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    box_rate = models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    image = models.ForeignKey(ProductImage,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)

    def __str__(self):
        return self.identity

    
     