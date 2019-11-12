from django.shortcuts import render
from django.http import HttpResponse
from food import models
# Create your views here.
def index(request):
    item_list = models.Item.objects.all()
    #template_index = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse('<h1>This is an itemview</h1>')

def detail(request,item_id):
    item=models.Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request,'food/detail.html',context)