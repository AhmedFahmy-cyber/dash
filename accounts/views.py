from django.shortcuts import render,redirect
from .forms import Orderform , Customerform ,Loginform ,Registerform
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.views.generic import TemplateView   

from .models import *


# Create your views here.
def registerPage(request):

    form = Registerform()
    if request.method == 'POST':
        form =Registerform(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request , 'Acount has been created for :' + username) 
            return redirect('login')
                      

    cotext ={'form':form}    

    return render (request ,'accounts/register.html',cotext)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (request ,username = username , password = password)
        if user is not None:
            
                login(request,user)

                return redirect ('dashboard')
        else:
            messages.info(request , 'username or password not correct ' )  
    cotext ={}

    return render (request ,'accounts/login.html',cotext)
def logOutuser(request):
    
    logout(request)
    
    return redirect  ('login')  

    
@login_required
def home(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    customers_total = customers.count()
    Orders_Delivered = orders.filter(status='Deliverd').count()
    Orders_Pending = orders.filter(status='Pending').count()
 
    context = {
        'customers': customers,
        'orders':orders,
        'Orders_Delivered':Orders_Delivered,
        'Orders_Pending':Orders_Pending,
        'customers_total':customers_total,
        'total_orders':total_orders,
    }
    return render(request , 'accounts/dashboard.html' ,context)

# class Home(LoginRequiredMixin,TemplateView):
#     template_name  =  'accounts/dashboard.html' 

@login_required
def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request , 'accounts/products.html',context)

# class Products(LoginRequiredMixin,TemplateView):
#     template_name  =  'accounts/products.html'     

def customers(request , pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer,
        'orders':orders,
        'order_count':order_count,
    }
    return render(request , 'accounts/customers.html',context)

def creatorder(request):

    form = Orderform()
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        'form':form,
        
    }
    return render(request , 'accounts/creat_form.html',context)


def placeNeworder(request , pk):
    customer = Customer.objects.get(id=pk)
    form = Orderform(initial={'customer':customer})
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        'form':form,
        
    }
    return render(request , 'accounts/creat_form.html',context)




def creatcustomer(request):
    
    form = Customerform()
    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        'form':form,
        
    }
    return render(request , 'accounts/creat_customer.html',context)

def updatecustomer(request , pk):
    customer = Customer.objects.get(id=pk)
    form = Customerform(instance=customer)
    
    if request.method == 'POST':
        form = Customerform(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        'customer':customer,
        'form':form,

    }
    return render(request , 'accounts/creat_customer.html',context)      

def updateorder(request , pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    
    if request.method == 'POST':
        form = Orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        'order':order,
        'form':form,

    }
    return render(request , 'accounts/creat_form.html',context)   


def deleteorder(request , pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    
    context = {
        'item':order,

    }
    return render(request , 'accounts/delete.html',context)    

