from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	"""
	Home view
	"""
	template_name = "index.html"
	return render_to_response(template_name)