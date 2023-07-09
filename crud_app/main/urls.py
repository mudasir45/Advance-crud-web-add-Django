from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('deleteStd/<int:id>', views.deleteStd, name='deleteStd'),
    path('updateStd/<int:id>', views.updateStd, name='updateStd'),
    
]