from django.urls import path
import officer.views

urlpatterns = [
    path('officerhome/',officer.views.officerhome,name='officerhome'),
    path('viewassigncase/', officer.views.viewassigncase, name='viewassigncase'),
    path('viewassigncase1/<id>', officer.views.viewassigncase1, name='viewassigncase1'),
    path('updatestatus/<id>', officer.views.updatestatus, name='updatestatus'),

]