from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name="home"),
    path('home/<str:document_field>',views.specific_docfield,name="home"),
    path('addDocument/',views.addDocument,name="addDocument"),
] 