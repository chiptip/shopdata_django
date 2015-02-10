from django.db import models
from elasticutils import MappingType

CATALOG_INDEX = 'catalog-index'
CATALOG_TYPE = 'external'

class Product(object):
	asin = models.CharField(max_length=150)
	title = models.CharField(max_length=150)
	category = models.CharField(max_length=150)
	manufacturer = models.CharField(max_length=150, null=True)
	url = models.CharField(max_length=255)
	catalog = models.ForeignKey(Catalog, related_name='items')

class Catalog(object):
	category = models.CharField(max_length=150)
	age = models.CharField(max_length=50)
	gender = models.CharField(max_length=15)
	source = models.CharField(max_length=150)
	order = models.CharField(max_length=150)
	timestamp = models.DateTimeField(auto_now_add=True)


class CatalogMappingType(MappingType, Indexable):

	@classmethod
	def get_index(cls):
		return CATALOG_INDEX

	@classmethod
	def get_mapping_type_name(cls):
		return CATALOG_TYPE

	@classmethod
	def get_model(cls):
		return Catalog

	@classmethod
	def get_mapping(cls):
		return {
			'properties': {
				'id': {'type': 'integer'},
				'category': {'type': 'string'},
				'age': {'type': 'string'},
				'gender': {'type': 'string'},
				'source': {'type': 'string'},
				'order': {'type': 'string'},
				'timestamp': {'type': 'string'},
				'items': {
					'type': 'nested',
					'include_in_parent': True,
					'properties': {
						'asin': {'type': 'string'},
						'title': {'type': 'string'},
						'category': {'type': 'string'},
						'manufacturer': {'type': 'string'},
						'url': {'type': 'string'}
					}
				}
			}
		}

	@classmethod
	def extract_document(cls, obj_id, obj=None):
		if obj == None:
			obj = cls.get_model().get(id=obj_id)

		doc = {}
		doc['id'] = obj.id
		doc['category'] = obj.category
		doc['age'] = obj.age
		doc['gender'] = obj.gender
		doc['source'] = obj.source
		doc['order'] = obj.order
		doc['timestamp'] = obj.timestamp
		doc['items'] = []
		for item in obj.items:
			product_doc = {}
			product_doc['asin'] = item.asin
			product_doc['title'] = item.title
			product_doc['category'] = item.category
			product_doc['manufacturer'] = item.manufacturer
			product_doc['url'] = item.url
			doc['items'].append(product_doc)
		return doc

	@classmethod
	def get_indexable(cls):
		return cls.get_model().get_objects()

	def get_object(self):
		return self.get_model().objects.get(pk=self._id)
