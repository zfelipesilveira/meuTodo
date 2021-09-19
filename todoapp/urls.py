from django.urls import path
from . import views

urlpatterns = [
    path('', views.alltodos, name = 'alltodos'),
    path('<int:pk>', views.deleteItem, name = 'deleteItem')
]