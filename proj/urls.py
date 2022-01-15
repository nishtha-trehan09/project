from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('display/<int:id>', views.display,name='display'),

   

]