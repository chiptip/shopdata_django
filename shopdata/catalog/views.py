from django.shortcuts import render
from django.views.generic import View
from shopdata.catalog.models import Catalog

# Create your views here.
class BrowseView(View):

	def get(self, request, gender='boy', age='21+'):
		catalog = Catalog.objects.get(age=age, gender=gender)
		data = {}
		return render(request, 'overview.html', data)

	def lookup_imgs(self, amazon_node_id):
		pass
