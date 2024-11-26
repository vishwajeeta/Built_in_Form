from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('api-info/',views.infolist,name="api-info"),
]