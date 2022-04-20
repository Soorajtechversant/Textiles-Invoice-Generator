from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('',views.index,name='home'),
    # path('buy/',views.buy,name='buy'),
    # path('pdf/',views.pdf,name='pdf'),
    path('bill/', views.bill, name='url'),
    # path('products',views.products),
    path('', views.home_view),
    path('indexview/', views.index),
    # path('adminclick/', views.adminclick_view),
    # path('adminsignup/', views.adminsignup_view),
    # path('adminlogin/', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),

    path('buyerclick/', views.buyerclick_view),

    path('buyersignup', views.buyersignup_view),

    path('buyerlogin/', LoginView.as_view(template_name='buyerlogin.html')),
    path('afterlogin/', views.afterlogin_view),

    path('contactus',views.contactus_view),
    path('buy/', views.buy),
    # path('buy/<int:pk>/',views.buy,name='buy'),
    path('pdf/',views.pdf,name='pdf'),


    # path('buy/<int:pk>/', views.buy, name='buy'),

    # path('pdf/', views.invoice),

    # path('pdf/', views.invoice, name='invoice'
    #
    # path('logout', LogoutView.as_view(template_name='homepage.html')),

]
