from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from elasticsearch import Elasticsearch
from shopdata.settings import ACCESS_KEY, ACCESS_SECRET, ASSOCIATE_ID
from shopdata.catalog.models import Catalog, Product

import amazonproduct

config = {
	'access_key': ACCESS_KEY,
	'secret_key': ACCESS_SECRET,
	'associate_tag': ASSOCIATE_ID,
	'locale': 'us'
}

api = amazonproduct.API(cfg=config)

# items = api.item_search('Books', Publisher="O'Reilly")
# for book in items:
# 	print '%s: "%s"' % (book.ItemAttributes.Author, book.ItemAttributes.Title)

# result = api.item_lookup('B006H3MIV8', ResponseGroup='Images')
# for item in result.Items.Item:
# 	print item.ASIN
# 	if item.LargeImage:
# 		print '%s - %s x %s' % (item.LargeImage.URL,
# 								item.LargeImage.Width,
# 								item.LargeImage.Height)
# http://ecx.images-amazon.com/images/I/61VWBOLaopL.jpg

# BrowseNode
TOY = ("Toys", 165793011)
BOY_TOY = ("Boys' Toys", 1263206011)
GIRL_TOY = ("Girl's Toys", 1263207011)

# try:
# 	l = List.objects.get(node_id=TOY[1])
# except ObjectDoesNotExist:
# 	l = List(node_id=TOY[1], name=TOY[0])
# 	l.save()


category = 'toys'
age = '14+'
gender = 'boys'
source = 'amazon'
order = 'new and popular'

catalog_doc = {
	'category': category,
	'age': age,
	'gender': gender,
	'source': source,
	'timestamp': datetime.now(),
	'order': order,
	'products': []
}

results = api.item_search('Toys', BrowseNode=165793011, responseGroup='Large')
counter = 0
for item in results:
	product_doc = {
		'asin': str(item.ASIN),
		'title': str(item.ItemAttributes.Title),
		'category': str(item.ItemAttributes.ProductGroup),
		'manufacturer': str(item.ItemAttributes.Manufacturer),
		'url': str(item.DetailPageURL)
	}
	catalog_doc['products'].append(product_doc)
	counter += 1
	if counter > 10:
		break

	add_db(catalog_doc)

def elastic_index(doc):
	es = Elasticsearch()
	es.index(
		index="catalog-index",
		doc_type="external",
		id=1,
		body=catalog_doc
	)

def add_db(doc):
	catalog = Catalog(catagory=doc['category'],
					  age=doc['age'],
					  gender=doc['gender'],
					  source=doc['source'],
					  order=doc['order'])
	catalog.save()

	for item in catalog['products']:
		product = Product(asin=item['asin'],
						  title=item['title'],
						  category=item['category'],
						  manufacturer=item['manufacturer'],
						  url=item['url'],
						  catalog=catalog)
		product.save()
