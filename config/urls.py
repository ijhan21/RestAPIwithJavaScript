#urls.py
from django.urls import include
from django.urls import re_path as url
from addresses import views
from django.urls import path
from anotherbrain import views as brain_views


urlpatterns = [
    path('subcategory/<int:subcategory>',brain_views.Question.as_view() ),
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]