from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from Admin.models import circle,station,designation,login
from citizen.models import complaint,missing,criminal,theft
from django.http import JsonResponse

from.models import officer,assigncase

# Create your views here.
def stationhome(request):
    return render(request, 'stationhome.html')
def officer1(request):
    if request.method=="POST":
        sid=request.session["uname"]
        sid1=station.objects.get(uname=sid)
        dname=request.POST.get("opn")
        did=designation.objects.get(id=dname)
        oname=request.POST.get("officername")
        gen=request.POST.get("gen")
        dob=request.POST.get("dob")
        address=request.POST.get("address")
        cnum=request.POST.get("cnum")
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd")
        o=officer()
        o.did=did.id
        o.address=address
        o.gender=gen
        o.uname=uname
        o.sid=sid1.id
        o.dob=dob
        o.password=pwd
        o.uname=uname
        o.contactnum=cnum
        o.officername=oname
        o.save()
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='officer'
        l.save()
        return HttpResponse("<script>alert('officer added successfully');window.location='/officer';</script>")



    else:
        d = designation.objects.all()
        context = {'k': d}
        template = loader.get_template("addofficer.html")
        return HttpResponse(template.render(context, request))

def viewcase(request):
    id=request.session["uname"]
    id1=station.objects.get(uname=id)
    s=complaint.objects.raw("select citizen_complaint.*,citizen_citizenreg.name,citizen_citizenreg.email,citizen_citizenreg.phone,citizen_citizenreg.hname,citizen_citizenreg.street,citizen_citizenreg.city,citizen_citizenreg.state,citizen_citizenreg.pin,citizen_citizenreg.country from citizen_citizenreg,citizen_complaint,admin_station where citizen_citizenreg.id=citizen_complaint.ctid and admin_station.id=citizen_complaint.sid and citizen_complaint.status='verify' and admin_station.id=%s",[id1.id])
    context = {'key': s}
    template = loader.get_template("assigncase.html")
    return HttpResponse(template.render(context, request))
def viewcase1(request,id):
    ctype=complaint.objects.get(id=id)
    suname=request.session["uname"]
    sid=station.objects.get(uname=suname)
    o=officer.objects.filter(sid=sid.id)
    if(ctype.ctype=="missing"):
        m=missing.objects.get(cid=id)
        context = {'key': m,'off':o}
        template = loader.get_template("assignmissing.html")
        return HttpResponse(template.render(context, request))
    elif (ctype.ctype == "criminal"):
        m = criminal.objects.get(cid=id)
        context = {'key': m, 'off': o}
        template = loader.get_template("assigncriminal.html")
        return HttpResponse(template.render(context, request))
    else:
        m = theft.objects.get(cid=id)
        context = {'key': m, 'off': o}
        template = loader.get_template("assigntheft.html")
        return HttpResponse(template.render(context, request))


def assignmissing(request,id):
    off=request.POST.get("opn")
    oid=officer.objects.get(id=off)
    asn=assigncase()
    asn.cmpid=id
    asn.offid=oid.id
    asn.status='pending'
    asn.save()
    c=complaint.objects.get(id=id)
    c.status='assign'
    c.cremarks=''
    c.save()
    return HttpResponse("<script>alert('case assigned successfully');window.location='/viewcase';</script>")

def stationviewstatus(request):
    uname=request.session["uname"]
    id=station.objects.get(uname=uname)
    c=complaint.objects.raw("select citizen_complaint.id,citizen_complaint.ctype,citizen_complaint.complaint,citizen_citizenreg.name,station_assigncase.status,station_assigncase.cremarks from citizen_citizenreg,citizen_complaint,station_assigncase,admin_station where citizen_complaint.id=station_assigncase.cmpid and citizen_complaint.ctid=citizen_citizenreg.id and citizen_complaint.sid=admin_station.id and citizen_complaint.status='complete' and admin_station.id=%s",[id.id])
    context={'key':c}
    template=loader.get_template("stationviewstatus.html")
    return HttpResponse(template.render(context,request))



