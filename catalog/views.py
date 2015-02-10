from django.shortcuts import render
from django.views.generic import View
from shopdata.catalog.views import Catalog

# Create your views here.
class Browse(View):

	def get(self, request):
		age = request.GET.get('age', default="21+")
		gender = request.GET.get('gender', default="boy")
        catalog = Catalog.objects.get(age=age, gender=gender)
        data = {}
        return render(request, 'overview.html', data)

	def lookup_imgs(self, amazon_node_id):
		pass
