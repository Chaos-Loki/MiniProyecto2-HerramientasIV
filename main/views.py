from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from . forms import CreateUserForm, ProductPostForm, CategoryPostForm
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
        Category,
    )
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
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

#funcion de crear producto
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
        

#-------------------------------------------------------------------------------------
#Vistas de Productos

class ProductView(generic.ListView):
    model = Product
    template_name = "main/store.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "main/product.html"

#----Vista de Edicion de Producto

class ProductEditView (LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'details', 'image', 'category']
    template_name = 'main/edit-products.html'
    
    def get_success_url(self):
        pk =self.kwargs['pk']
        return reverse_lazy('product', kwargs={'pk': pk})

#----Vista de Eliminacion de Producto

class ProductDeleteView (LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/delete-products.html'
    success_url= reverse_lazy('store')
    
    
    
#-------------------------------------------------------------------------------------
#Vistas de Categorias

class ProductView(generic.ListView):
    model = Category
    template_name = "main/categories.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "main/category.html"

#----Vista de Edicion de Categorias

class CategoryEditView (LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'description', 'details', 'image', 'category']
    template_name = 'main/edit-category.html'
    
    def get_success_url(self):
        pk =self.kwargs['pk']
        return reverse_lazy('product', kwargs={'pk': pk})

#----Vista de Eliminacion de Categorias

class CategoryDeleteView (LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'main/delete-category.html'
    success_url= reverse_lazy('store')
    



#Vista de Index - Defecto

class IndexView(generic.TemplateView):
        template_name = "main/index.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
        