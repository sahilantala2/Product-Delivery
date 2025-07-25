from django.urls import path
from GameStore import views


urlpatterns = [
    path('', views.home,name='home'),
    path('customer/<int:cus_id>/', views.customer,name='customer'),
    path('products/', views.products,name='product'),
    path('update_customer/<int:id>', views.update_customer,name='update_customer'),
    path('delete_customer/<int:id>', views.delete_customer,name='delete_customer'),
    path('create_order/', views.create_order,name='create_order'),
    path('create_customer/', views.create_customer,name='create_customer'),
    path('updateorder/<int:id>', views.update_order,name='updateorder'),
    path('delete_order/<int:id>', views.delete_order,name='delete_order'),
    path('login_page', views.login_page,name='login_page'),
    path('register_page', views.register_page,name='register_page'),
]