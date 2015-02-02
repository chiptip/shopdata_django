import amazonproduct

config = {
	'access_key': 'AKIAIIXOTMRH2AZMQKJA',
	'secret_key': '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',
	'associate_tag': 'shopdata-20',
	'locale': 'us'
}

api = amazonproduct.API(cfg=config)

items = api.item_search('Books', Publisher="O'Reilly")
for book in items:
	print '%s: "%s"' % (book.ItemAttributes.Author, book.ItemAttributes.Title)
