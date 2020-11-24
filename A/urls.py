from django.urls import path
from A import views
urlpatterns = [
    path('', views.ViewsA, name="ViewsA")
]
