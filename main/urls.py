from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.IndexView.as_view(), name="home"),
    #EN SUCESION, ESTOS SON PERFILES Y TIENDA/LISTA DE PRODUCTOS
    path('profiles/', views.ProfileView.as_view(), name="profiles"),
    path('store/', views.ProductView.as_view(), name="store"),
    #SECCION DE CATEGORIAS, adicion y productos
    path('add-categories/', views.IndexView.as_view(), name="add-categories"),
    path('edit-categories/', views.IndexView.as_view(), name="edit-categories"),
    path('delete-categories/', views.IndexView.as_view(), name="delete-categories"),
    path('category/', views.IndexView.as_view(), name="category"),
    #SECCION DE PRODUCTOS - añadir, edicion, eliminacion y producto
    path('add-products/', views.ProductCreatePage, name="add-products"),
    path('edit-products/<int:pk>', views.ProductEditView.as_view(), name="edit-products"),
    path('delete-products/<int:pk>', views.ProductDeleteView.as_view(), name="delete-products"),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name="product"),	
]
