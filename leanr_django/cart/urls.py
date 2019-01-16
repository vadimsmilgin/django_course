from django.urls import path, re_path
from cart import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    path('', views.CartDetail, name='CartDetail'),
]