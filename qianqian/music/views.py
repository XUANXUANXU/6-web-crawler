from django.shortcuts import render
from .models import Qianqian
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def music_list(resquest):
    singlist = Qianqian.objects.all()
    data = []
    data = serializers.serialize('json', singlist)
    return HttpResponse(data, content_type='application/json')


