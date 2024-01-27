from django.urls import path
import station.views

urlpatterns = [
    path('stationhome/', station.views.stationhome, name='stationhome'),
    path('officer/', station.views.officer1, name='officer'),
    path('viewcase/', station.views.viewcase, name='viewcase'),
    path('viewcase1/<id>', station.views.viewcase1, name='viewcase1'),
    path('assignmissing/<id>', station.views.assignmissing, name='assignmissing'),
    path('stationviewstatus/', station.views.stationviewstatus, name='stationviewstatus'),

]