from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.IndexView.as_view(), name="home"),
    path('categories/', views.IndexView.as_view(), name="categories"),
    path('add-products/', views.IndexView.as_view(), name="add-products"),
    path('store/', views.ProductView.as_view(), name="store"),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name="product"),	
]
