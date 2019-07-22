from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('detail/<int:id>', views.product_detail, name = 'productdetail'),
    path('products/', views.product_list, name = 'productlist'),
    path('home/', views.home_page),
]