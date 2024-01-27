from django.urls import path
import Admin.views

urlpatterns = [
path('',Admin.views.index,name='index'),
path('login/',Admin.views.login1,name='login'),
path('adminhome/',Admin.views.adminhome,name='adminhome'),
path('designation/',Admin.views.designation1,name='designation'),
path('district/',Admin.views.district1,name='district'),
path('circle/',Admin.views.circle1,name='circle'),
path('station/',Admin.views.station1,name='station'),
path('viewdesig/',Admin.views.viewdesignation1,name='viewdesig'),
path('desigdelete/<id>', Admin.views.desigdelete1,name='desigdelete'),
path('desigedit/<id>', Admin.views.desigedit1, name='desigedit'),
path('desigupdate/<id>', Admin.views.desigupdate1, name='desigupdate'),
path('viewdis/',Admin.views.viewdistrict2,name='viewdis'),
path('disdelete/<id>', Admin.views.disdelete2,name='disdelete'),
path('disedit/<id>', Admin.views.disedit2, name='disedit'),
path('disupdate/<id>', Admin.views.disupdate2, name='disupdate'),
path('viewcitizen/',Admin.views.viewcitizen,name='viewcitizen'),
path('approvecitizen/<id>',Admin.views.approvecitizen,name='approvecitizen'),
path('rejectcitizen/<id>',Admin.views.rejectcitizen,name='rejectcitizen'),
path('viewlawer/',Admin.views.viewlawer,name='viewlawer'),
path('approvelawer/<id>',Admin.views.approvelawer,name='approvelawer'),
path('rejectlawer/<id>',Admin.views.rejectlawer,name='rejectlawer'),
path('updatedesig/',Admin.views.desigedit1,name='updatedesig'),
path('viewcircle/',Admin.views.viewcircle,name='viewcircle'),
path('circledelete/<id>', Admin.views.circledelete,name='circledelete'),
path('circleedit/<id>', Admin.views.circleedit, name='circleedit'),
path('circleupdate/<id>', Admin.views.circleupdate, name='circleupdate'),
path('viewstation/',Admin.views.viewstation,name='viewstation'),
path('stationdelete/<id>', Admin.views.stationdelete,name='stationdelete'),
path('stationedit/<id>', Admin.views.stationedit, name='stationedit'),
path('stationupdate/<id>', Admin.views.stationupdate, name='stationupdate'),
path('viewlawer1/<id>', Admin.views.viewlawer1, name='viewlawer1'),
path('verifycomplaint/', Admin.views.verifycomplaint, name='verifycomplaint'),
path('viewdetails/<id>', Admin.views.viewdetails, name='viewdetails'),
path('verifymissing/<id>', Admin.views.verifymissing, name='verifymissing'),
path('verifycriminal/<id>', Admin.views.verifycriminal, name='verifycriminal'),
path('verifytheft/<id>', Admin.views.verifytheft, name='verifytheft'),
path('adminviewcasestatus/', Admin.views.adminviewcasestatus, name='adminviewcasestatus'),

path('adminviewmissing/<id>', Admin.views.adminviewmissing, name='adminviewmissing'),
path('npwd', Admin.views.npwd, name='npwd'),



]