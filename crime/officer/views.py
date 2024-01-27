from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from station.models import officer,assigncase
from citizen.models import complaint,missing,criminal,theft
# Create your views here.
def officerhome(request):
    return render(request, 'officerhome.html')
def viewassigncase(request):
    uname=request.session["uname"]
    ofid=officer.objects.get(uname=uname)
    s=complaint.objects.raw("select citizen_complaint.*,citizen_citizenreg.name,citizen_citizenreg.email,citizen_citizenreg.phone,citizen_citizenreg.hname,citizen_citizenreg.street,citizen_citizenreg.city,citizen_citizenreg.state,citizen_citizenreg.pin,citizen_citizenreg.country from citizen_citizenreg,citizen_complaint,station_officer,station_assigncase where citizen_citizenreg.id=citizen_complaint.ctid and station_officer.id=station_assigncase.offid and citizen_complaint.status='assign' and station_assigncase.cmpid=citizen_complaint.id and station_officer.id=%s",[ofid.id])

    context={'key':s}
    template=loader.get_template("viewassigncase.html")
    return HttpResponse(template.render(context,request))
def viewassigncase1(request,id):
    ctype = complaint.objects.get(id=id)


    if (ctype.ctype == "missing"):
        m = missing.objects.get(cid=id)
        context = {'key': m}
        template = loader.get_template("viewassignmissing.html")
        return HttpResponse(template.render(context, request))
    elif (ctype.ctype == "criminal"):
        m = criminal.objects.get(cid=id)
        context = {'key': m}
        template = loader.get_template("viewassigncriminal.html")
        return HttpResponse(template.render(context, request))
    else:
        m = theft.objects.get(cid=id)
        context = {'key': m}
        template = loader.get_template("viewassigntheft.html")
        return HttpResponse(template.render(context, request))
def updatestatus(request,id):
    c=complaint.objects.get(id=id)



    m=assigncase.objects.get(cmpid=id)
    status=request.POST.get("status")
    crem=request.POST.get("cremarks")
    m.status=status
    m.cremarks=crem
    m.save()

    c.status = 'complete'
    c.save()
    return HttpResponse("<script>alert('case completed successfully');window.location='/viewassigncase';</script>")



