from django.urls import path
import lawer.views

urlpatterns = [
    path('lawerhome/', lawer.views.lawerhome, name='lawerhome'),
    path('lawerreg/',lawer.views.lawerreg1,name='lawerreg'),
    path('lawerviewcase/', lawer.views.lawerviewcase, name='lawerviewcase'),
    path('lawerviewdetails/<id>',lawer.views.lawerviewdetails,name='lawerviewdetails'),
    path('lawerchangepass/',lawer.views.lawerchangepass,name='lawerchangepass'),


]