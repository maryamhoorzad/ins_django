from django.conf.urls import url
from django.urls import path
from . import views
from .views import product_detail,product_list,home_page

app_name = 'store'

urlpatterns = [
    path('detail/<int:id>', views.product_detail),
    path('products/', views.product_list),
    path('home/', views.home_page),
]