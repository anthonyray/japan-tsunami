from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template.response import TemplateResponse, SimpleTemplateResponse
from japan_map.models import Japan
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect


#will be given by the user later
lat_tsunami = 34.241238
lon_tsunami = 137.433197
rad = 500

@requires_csrf_token
def japan_map(request):
	c = {}

	j = Japan()
	template = 'japan_map.html'
	title = "Japan Tsunami Map"
	datas = j.get_people()
	japan_cities = j.get_cities()

	

	return render(request, template, {"title":title,"datas":datas,"latTsunami":lat_tsunami,"lonTsunami":lon_tsunami,"japancities":japan_cities})

	'''return SimpleTemplateResponse( template, {"title":title,"datas":datas,"latTsunami":lat_tsunami,"lonTsunami":lon_tsunami,"japancities":japan_cities})'''


