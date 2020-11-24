from django.urls import path

from C import views

urlpatterns = [
    path('', views.ViewsC, name="ViewsC")
]
