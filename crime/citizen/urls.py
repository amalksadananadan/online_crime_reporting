from django.urls import path
import citizen.views

urlpatterns = [
path('citizenhome/',citizen.views.citizenhome,name='citizenhome'),
path('complaint/',citizen.views.complaint1,name='complaint'),
path('missing/',citizen.views.missing1,name='missing'),
path('theft/',citizen.views.theft1,name='theft'),
path('criminal/',citizen.views.criminal1,name='criminal'),
path('citizenreg/',citizen.views.citizenreg1,name='citizenreg'),
path('sortdistrict/',citizen.views.sortdistrict,name='sortdistrict'),
path('sortcircle/',citizen.views.sortcircle,name='sortcircle'),
path('citizenviewstatus/',citizen.views.citizenviewstatus,name='citizenviewstatus'),
path('searchlawer/<id>',citizen.views.searchlawer,name='searchlawer'),
path('selectlawer/<id>',citizen.views.selectlawer,name='selectlawer'),
path('citizenchangepass/',citizen.views.citizenchangepass,name='citizenchangepass'),






]