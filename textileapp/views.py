from django.shortcuts import render
from .models import *
from django.contrib.auth import login, authenticate

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required,user_passes_test
import datetime

# Create your views here.
from .forms import *


def index(request):
    return render(request, 'indexpage.html')


# actual
#
# def buy(request):
#     # print()
#     pro = productz.objects.get()   #(pk=pk)
#
#     if request.method == "POST":
#         name = request.POST['name']
#         address = request.POST['address']
#         phone = request.POST['phone']
#         quantity = int(request.POST['quantity'])
#
#         by = buyer(name=name, address=address, phone=phone)
#         by.save()
#         amount = float(pro.price)
#         pn = pro.name
#         dis = pro.dis
#         price = amount
#         pro_quantity = quantity
#         pro_total = amount * quantity
#         slr = seller.objects.all()
#         data = {'pname': pn, 'pprice': price, 'bname': name, 'baddress': address, 'bphone': phone, 'pdis': dis,
#                 'pquantity': pro_quantity, 'ptotal': pro_total}
#         return render(request, 'pdf.html', {'data': data, 'seller': slr})
#
#     return render(request, 'buy.html')
#
#
def pdf(request):
    slr = seller.objects.all()
    return render(request, 'pdf.html', {'seller': slr})



# exception
#
# def buy(request):
#     if request.method == "POST":
#         a = Bills(request.POST)
#         if a.is_valid():
#             nm = a.cleaned_data['Name']
#             em = a.cleaned_data['Price']
#             ph = a.cleaned_data['Quantity']
#             b = Billing(Name=nm, Price=em, Quantity=ph)
#             b.save()
#             total = em * ph
#             return render(request, 'bill.html', {'name': nm, 'total': total})
#         else:
#             return HttpResponse("Error in details")
#     else:
#         return render(request, 'buy.html')


#normal
def buy(request):
    if request.method == "POST":
        a = Bills(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['Name']
            ad = a.cleaned_data['Address']
            pho = a.cleaned_data['Phone']
            qua = a.cleaned_data['Quantity']
            b = Billing(Name=nm, Address=ad, Phone=pho, Quantity=qua, )
            b.save()
            # total = em * qua
            return render( request,'bill.html', {'name': nm,'phone':pho,'address':ad,'quantity':qua})
        else:
            return HttpResponse("Error in details")
    else:
        return render(request, 'buy.html')


#used primary key

# def buy(request, pk):
#     print(pk)
#     pro = productz.objects.get(pk=pk)
#
#     if request.method == "POST":
#         name = request.POST['name']
#         address = request.POST['address']
#         phone = request.POST['phone']
#         quantity = int(request.POST['quantity'])
#
#         by = buyer(name=name, address=address, phone=phone)
#         by.save()
#         amount = float(pro.price)
#         pn = pro.name
#         dis = pro.dis
#         price = amount
#         pro_quantity = quantity
#         pro_total = amount * quantity
#         slr = seller.objects.all()
#         data = {'pname': pn, 'pprice': price, 'bname': name, 'baddress': address, 'bphone': phone, 'pdis': dis,
#                 'pquantity': pro_quantity, 'ptotal': pro_total}
#         return render(request, 'pdf.html', {'data': data, 'seller': slr})
#
#     return render(request, 'buy.html')
#

#
# def index_view(request):
#     return render(request,'indexpage.html')

def home_view(request):
    return render(request, 'homepage.html')

# def products(request):
#     return render(request,'products.html')

def adminclick_view(request):
    return render(request, 'adminclick.html')


def adminsignup_view(request):
    form = AdminSignupForm()
    if request.method == 'POST':
        a = AdminSignupForm()
        if a.is_valid():
            user = a.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return redirect('adminlogin')  # url
    return render(request, 'adminsignup.html', {'form': form})


def is_buyer(user):
    return user.groups.filter(name='BUYER').exists()



def afterlogin_view(request):
     if is_buyer(request.user):
         return render(request, 'indexpage.html')
     else:
        return redirect ('homepage')


#
# def login_buyer(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect('indexview')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name='buyerlogin.html', context={"login_form": form})
#

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)

def buyerclick_view(request):
    return render(request, 'buyerclick.html')


def buyersignup_view(request):
    form1 = BuyerForm()

    mydict = {'form1': form1}
    if request.method == 'POST':
        form1 = BuyerForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            my_buyer_group = Group.objects.get_or_create(name='BUYER')
            my_buyer_group[0].user_set.add(user)

        return HttpResponseRedirect('buyerlogin')
    return render(request, 'buyersignup.html', context=mydict)

def contactus_view(request):

    return render(request, 'contactus.html')

def bill(request):
    return render(request,'bill.html')