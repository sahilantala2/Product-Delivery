from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

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

    path('login_page/', views.login_page,name='login_page'),
    path('logout/', views.logoutUser,name='logout'),

    path('register_page/', views.register_page,name='register_page'),
    path('user_page/',views.userpage,name="user_page"),

    path('profile',views.profile_page,name="profile"),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="reset_password_sent"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),



]