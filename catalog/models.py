from django.db import models

# Create your models here.
class Product:
	asid = models.CharField(max_length=50)


class List:
	node_id = models.IntegerField()
	name = models.CharField(max_length=50)
	products = models.ForeignKey(Product)
