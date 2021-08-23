from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name="home"),
    path('home/<str:document_name>',views.specific_docfield,name="home"),
    path('addDocument/',views.addDocument,name="addDocument"),
    path('home/download/<str:document_name>/<str:document_version>',views.download,name="download"),
    path('logout/',views.logout,name="logout"),
] 