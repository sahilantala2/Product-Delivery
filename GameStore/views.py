from tokenize import group
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from pyexpat.errors import messages
from django.contrib import messages
from .filters import OrderFilter
from .models import *
from .forms import OrderForm,CreateUseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username Or Password is incorrect')
            # return render(request,'login.html')

    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login_page')

@unauthenticated_user
def register_page(request):
    form = CreateUseForm()
    if request.method == 'POST':
        form=CreateUseForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group=Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request,'Account was created for: ' + username)
            return redirect('login_page')

    context = {
        'form':form
    }
    return render(request,'register.html',context)

@login_required(login_url='/login_page/')
# @allowed_users(allowed_roles=['admin'])
@admin_only
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

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin','customer'])
def products(request):
    products_data = Product_item.objects.all()
    context ={'product':products_data}
    return render(request,'product.html',context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def customer(request,cus_id):
    custo = Customer.objects.get(id=cus_id)
    ord_count = custo.order_set.count()
    orders = custo.order_set.all()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    context = {
        'customer_data': custo,
        'order_data' : orders,
        'ord_count' : ord_count,
        'my_filter': my_filter
    }
    return render(request,'customer.html',context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    orders = request.user.customer.order_set.all()

    print(orders)
    context = {'orders': orders}
    return render(request,'user_page.html',context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def create_customer(req):
    forms = CustomerForm()
    if req.method == 'POST':
        forms = CustomerForm(req.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context = {
        'form':forms
    }
    return render(req,'create_customer.html',context=context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def update_customer(req,id):
    customer_data = Customer.objects.get(id=id)
    forms = CustomerForm(instance=customer_data)
    if req.method == 'POST':
        forms = CustomerForm(req.POST, instance=customer_data)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {
            'form':forms
        }
    return render(req,'create_customer.html',context=context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def delete_customer(req,id):
    customer_delete = Customer.objects.get(id=id)
    if req.method == 'POST':
        customer_delete.delete()
        return redirect('/')
    context = {
        'form': customer_delete
    }

    return render(req,'delete_customer.html')

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def create_order(req):
    forms = OrderForm()
    if req.method == 'POST':
        forms = OrderForm(req.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context = {
        'form':forms
    }

    return render(req,'create_order.html',context=context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def update_order(req, id):
    order = Order.objects.get(id=id)
    forms = OrderForm(instance=order)
    if req.method == 'POST':
        forms = OrderForm(req.POST,instance=order)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context = {
        'form' : forms
    }
    return render(req,'create_order.html',context=context)

@login_required(login_url='/login_page/')
@allowed_users(allowed_roles=['admin'])
def delete_order(req, id):
    order = Order.objects.get(id=id)
    if req.method == 'POST':
        order.delete()
        return  redirect('/')
    context = {
        'form' : order
    }
    return render(req,'delete_order.html',context=context)

def profile_page(req):


    context = {}
    return render(req, 'profile.html',context)