from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Apicursos', views.ApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('home',views.home, name="home"),
]