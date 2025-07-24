from django.urls import path
from GameStore import views


urlpatterns = [
    path('', views.home,name='home'),
    path('customer/<cus_id>/', views.customer,name='customer'),
    path('products/', views.products,name='product'),
    path('update_customer/', views.update_customer,name='update_customer'),
    path('delete_customer/', views.delete_customer,name='delete_customer'),
    path('create_order/', views.create_order,name='create_order'),
]