from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from . forms import CreateUserForm, ProductPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.cache import cache_control
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
        UserProfile,
        Product,
        Categories,
    )

# Create your views here.

#Funcion de Registro
def registerPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'main/register.html', context)
#Funcion de Login

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:home")
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'main/login.html', context)

#Funcion de Logout
def logoutUser(request):
    logout(request)
    return redirect('main:login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def ProductCreatePage(request):
    if request.method == 'POST':
        form = ProductPostForm(request.POST, request.FILES)	
        if form.is_valid():
            entrada = form.save()
            messages.success(request, "Se añadio producto satisfactoriamente!")
            return redirect('/')
        else:
            messages.error(request, "Hubo un error... verifique e intentelo de nuevo.")
            form = ProductPostForm()
    else:
        form = ProductPostForm()
    return render(request, "main/add-products.html", {'form':form})

#Vista de Perfil - mixin es usado para protegerlo

class ProfileView(LoginRequiredMixin, TemplateView):
        template_name = "main/profiles.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
        
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url='main:login')
# def blogCreatePage(request):
# 	if request.method == 'POST':
# 		form = BlogPostForm(request.POST, request.FILES)	
# 		if form.is_valid():
# 			entrada = form.save()
# 			messages.success(request, "Se añadio post satisfactoriamente!")
# 			return redirect('/')
# 	else:
# 		form = BlogPostForm()
# 	return render(request, "main/blog-create.html", {'form':form}


#Vistas de Productos

class ProductView(generic.ListView):
    model = Product
    template_name = "main/store.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "main/product.html"

#Vista de Index - Defecto

class IndexView(generic.TemplateView):
        template_name = "main/index.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
        