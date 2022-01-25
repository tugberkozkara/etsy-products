from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    img_url = models.URLField()
    price = models.CharField(max_length=10)
    class Meta:
        db_table = "products"