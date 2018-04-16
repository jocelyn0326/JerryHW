from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import Person

def index(request):
	people=Person.objects.all()
	return render_to_response('jocelyn/introduce.html',locals())

