from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage,name="register"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logOutuser,name="logout"),
    path('', views.home ,name="dashboard"),
    path('products/', views.products ,name="products"),
    path('customer/<str:pk_test>/', views.customers,name="customer"),
    path('creat_order/', views.creatorder,name="creat_order"),
    path('creat_customer/', views.creatcustomer,name="creat_customer"),
    path('update_order/<str:pk>/', views.updateorder,name="update_order"),
    path('update_customer/<str:pk>/', views.updatecustomer,name="update_customer"),
    path('place_new_order/<str:pk>/', views.placeNeworder,name="place_new_order"),
    path('delete_order/<str:pk>/', views.deleteorder,name="delete_order"),
]

