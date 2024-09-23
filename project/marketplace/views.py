from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mango, Order
from .forms import MangoForm, TreeDetailsForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login





from django.contrib.auth import login as auth_login, logout, authenticate

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Mango, Order
from .forms import MangoForm, TreeDetailsForm



def home(request):
    return render(request, 'marketplace/home.html')

@login_required
def mango_marketplace(request):
    if request.user.is_authenticated:
        return render(request, 'marketplace/marketplace.html')
    return redirect('login')
  
'''@login_required
def seller_view(request):
    if request.method == 'POST':
        mango_form = MangoForm(request.POST, request.FILES)
        tree_form = TreeDetailsForm(request.POST, request.FILES)
        if mango_form.is_valid() and tree_form.is_valid():
            mango = mango_form.save(commit=False)
            mango.seller = request.user
            mango.save()
            tree_details = tree_form.save(commit=False)
            tree_details.mango = mango
            tree_details.save()
            return redirect('marketplace')
    else:
        mango_form = MangoForm()
        tree_form = TreeDetailsForm()
    return render(request, 'marketplace/seller.html', {'mango_form': mango_form, 'tree_form': tree_form})'''
@login_required
def seller_view(request):
    if request.method == 'POST':
        mango_form = MangoForm(request.POST, request.FILES)
        tree_form = TreeDetailsForm(request.POST, request.FILES)
        if mango_form.is_valid() and tree_form.is_valid():
            mango = mango_form.save(commit=False)
            mango.seller = request.user
            mango.save()
            tree_details = tree_form.save(commit=False)
            tree_details.mango = mango
            tree_details.save()
            return redirect('marketplace')
    else:
        mango_form = MangoForm()
        tree_form = TreeDetailsForm()
    return render(request, 'marketplace/seller.html', {'mango_form': mango_form, 'tree_form': tree_form})


@login_required
def buyer_view(request):
    mangoes = Mango.objects.all()
    return render(request, 'marketplace/buyer.html', {'mangoes': mangoes})

@login_required
def place_order(request, mango_id):
    mango = Mango.objects.get(id=mango_id)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        order = Order.objects.create(buyer=request.user, mango=mango, quantity=quantity)
        # Send notification logic here
        return redirect('marketplace')
    return render(request, 'marketplace/place_order.html', {'mango': mango})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'marketplace/signup.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next', 'home'))
    else:
        form = AuthenticationForm()
    return render(request, 'marketplace/login.html', {'form': form})



# marketplace/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mango

@login_required
def seller_products(request):
    mangoes = Mango.objects.filter(seller=request.user)
    return render(request, 'marketplace/seller_products.html', {'mangoes': mangoes})

@login_required
def delete_mango(request, mango_id):
    mango = get_object_or_404(Mango, id=mango_id, seller=request.user)
    if request.method == "POST":
        mango.delete()
        messages.success(request, "Mango listing deleted successfully.")
        return redirect('seller_products')
    return render(request, 'marketplace/confirm_delete.html', {'mango': mango})





