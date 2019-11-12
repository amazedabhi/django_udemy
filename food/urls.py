from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [
    #/food/hello/
    path('hello/',views.index,name='index'),
    #/food/item/
    path('item/',views.item,name='item'),
    #/food/1
    path('<int:item_id>/',views.detail,name='detail'),
]