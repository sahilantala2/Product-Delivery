from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import *


# Create your views here.


def home(request):
    customer_data = Customer.objects.all()
    products_data = Product_item.objects.all()
    orders = Order.objects.all()
    ord_count = orders.count()
    order_status_deliver = orders.filter(status = "Delivered")
    order_status_deliver = order_status_deliver.count()
    order_status_pending = orders.filter(status = "Pending")
    order_status_pending = order_status_pending.count()

    context ={'customer':customer_data ,'product' : products_data, 'total_orders':ord_count, 'total_deliver':order_status_deliver, 'total_pending':order_status_pending,'orders':orders }
    return render(request,'index.html',context)

def products(request):
    products_data = Product_item.objects.all()
    context ={'product':products_data}
    return render(request,'product.html',context)

def customer(request,cus_id):
    custo = Customer.objects.get(id=cus_id)
    ord_count = custo.order_set.count()
    orders = custo.order_set.all()

    context = {
        'customer_data': custo,
        'order_data' : orders,
        'ord_count' : ord_count
    }
    return render(request,'customer.html',context)

def update_customer(req):
    return render(req,'update_customer.html')

def delete_customer(req):
    return render(req,'delete_customer.html')

def create_order(req):
    return render(req,'create_order.html')
