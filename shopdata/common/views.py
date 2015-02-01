# some_app/views.py
from django.views.generic import TemplateView
from django.shortcuts import render

class ProfileView(TemplateView):
	template_name = "profile.html"

	def get(self, request):
		access_token = request.GET.get('access_token')
		return render(request, self.template_name, {'token': access_token})
