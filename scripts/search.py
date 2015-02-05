from shopdata.settings import ACCESS_KEY, ACCESS_SECRET, ASSOCIATE_ID
from catalog.models import List, Product
from django.core.exceptions import ObjectDoesNotExist
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
TOY = ('Toys', 165793011)

try:
	l = List.objects.get(node_id=TOY[1])
except ObjectDoesNotExist:
	l = List(node_id=TOY[1], name=TOY[0])
	l.save()

result = api.browse_node_lookup(TOY[0], 'TopSellers')
for item in result.BrowseNodes.BrowseNode.TopSellers.TopSeller:
	p = Product.objects.create(name=item.Name, asid=item.ASID)
	
