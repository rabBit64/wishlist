from django.urls import path
from . import views
app_name = 'shoppings'
urlpatterns = [
  path('',views.index, name='index'),
]