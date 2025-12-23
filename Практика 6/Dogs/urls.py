from django.urls import path
import views

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.show_images, name='images'),
]

