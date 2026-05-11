from django.urls import path
from todo1 import views

urlpatterns = [
    path("",views.index),
    path("<int:id>/",views.delete,name="delete")
]
