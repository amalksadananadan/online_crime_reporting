from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from .models import lawyerreg
from Admin.models import login
from citizen.models import complaint,criminal,missing,theft


# Create your views here.
def lawerhome(request):
    return render(request, 'lawerhome.html')
def lawerreg1(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        hname=request.POST.get("hname")
        street=request.POST.get("street")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        country=request.POST.get("country")
        uname=request.POST.get("uname")
        pwd = request.POST.get("pwd")
        photo=request.FILES["photo"]
        qual = request.FILES["qual"]
        proof = request.FILES["proof"]
        s=lawyerreg()
        s.name=name
        s.email=email
        s.phone=phone
        s.hname=hname
        s.street=street
        s.city=city
        s.state=state
        s.pin=pin
        s.country=country
        s.photo=photo
        s.qual=qual
        s.proof=proof
        s.uname=uname
        s.pwd=pwd
        s.status='pending'
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='lawyer'
        l.save()
        s.save()

        return HttpResponse("<script>alert('Register successfully');window.location='/lawerreg';</script>")

    else:
        context={}
        template=loader.get_template("lawerreg.html")
        return HttpResponse(template.render(context,request))
def lawerviewcase(request):
    uname=request.session["uname"]
    id=lawyerreg.objects.get(uname=uname)
    c=complaint.objects.raw("SELECT citizen_complaint.*,admin_station.sname,admin_station.scode,station_officer.officername,citizen_citizenreg.name,citizen_citizenreg.phone from citizen_complaint,citizen_citizenreg,admin_station,station_officer,citizen_selectedlawer,station_assigncase,lawer_lawyerreg where admin_station.id=station_officer.sid and station_officer.id=station_assigncase.offid and station_assigncase.cmpid=citizen_complaint.id and citizen_complaint.ctid=citizen_citizenreg.id and citizen_selectedlawer.cmpid=citizen_complaint.id and  lawer_lawyerreg.id=citizen_selectedlawer.lid and  citizen_selectedlawer.lid=%s",[id.id])
    context = {'key':c}
    template = loader.get_template("lawerviewcase.html")
    return HttpResponse(template.render(context, request))
def lawerviewdetails(request,id):
    id1=complaint.objects.get(id=id)
    if(id1.ctype=="missing"):
        c=missing.objects.get(cid=id)
        context = {'key': c}
        template = loader.get_template("lawerviewmissing.html")
        return HttpResponse(template.render(context, request))
    elif(id1.ctype=="criminal"):
        c=criminal.objects.get(cid=id)
        context = {'key': c}
        template = loader.get_template("lawerviewcriminal.html")
        return HttpResponse(template.render(context, request))
    else:
        c = theft.objects.get(cid=id)
        context = {'key': c}
        template = loader.get_template("lawerviewtheft.html")
        return HttpResponse(template.render(context, request))
def lawerchangepass(request):
    if request.method=="POST":
        uname=request.session["uname"]
        opwd=request.POST.get("opwd")
        npwd=request.POST.get("npwd")
        l=login.objects.raw("SELECT * from admin_login where uname=%s and pwd=%s",[uname,opwd])
        if not l:
            return HttpResponse("<script>alert('Invalid Password');window.location='/lawerchangepass';</script>")
        else:
            l=login.objects.get(uname=uname,pwd=opwd)
            l.pwd=npwd
            l.save()
            c=lawyerreg.objects.get(uname=uname)
            c.pwd=npwd
            c.save()
            return HttpResponse("<script>alert('Password Changed Successfully');window.location='/lawerchangepass';</script>")



    else:
        uname=request.session["uname"]
        context = {'key': uname}
        template = loader.get_template("lawerchangepass.html")
        return HttpResponse(template.render(context, request))



