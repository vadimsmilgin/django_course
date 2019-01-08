from shop.views import *
from django.urls import path, re_path

urlpatterns = [
    path('', ProductList.as_view()),
    re_path(r'^(?P<slug>[-\w]+)$', SingleProduct.as_view(), name='detail'),
]