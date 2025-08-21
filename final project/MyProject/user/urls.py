from django.urls import path
from . import views

urlpatterns=[
   path('index/',views.index),
   path('',views.index),
   path('about/',views.about),
   path('contact/',views.contact),
   path('registration/',views.signup),
   path('login/',views.studentlogin),
   path('feedback/',views.feedback),
   path('newbatches/',views.newbatchess),
   path('ourfacility/',views.ourfacility),
   path('ourplacements/',views.successstories),






]