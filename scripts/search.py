from shopdata.settings import ACCESS_KEY, ACCESS_SECRET, ASSOCIATE_ID
import amazonproduct

config = {
	'access_key': ACCESS_KEY,
	'secret_key': ACCESS_SECRET,
	'associate_tag': ASSOCIATE_ID,
	'locale': 'us'
}

api = amazonproduct.API(cfg=config)

items = api.item_search('Books', Publisher="O'Reilly")
for book in items:
	print '%s: "%s"' % (book.ItemAttributes.Author, book.ItemAttributes.Title)
