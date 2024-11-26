from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('api-info/',views.infolist,name="api-info"),
    path('api-info-detail/<str:pk>/',views.infolistdetail,name="api-info-detail"),
    path('api-info-create/',views.infolistcreate,name="api-info-create"),
    path('api-info-update/<str:pk>/',views.infolistupdate,name="api-info-update"),
    path('api-info-delete/<str:pk>/',views.infolistdelete,name="api-info-delete"),
]