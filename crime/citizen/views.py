from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from .models import citizenreg,complaint,missing,criminal,theft,selectedlawer
from Admin.models import login,district,circle,station,login
from lawer.models import lawyerreg
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
def citizenhome(request):
    return render(request, 'citizenhome.html')

def complaint1(request):
    if request.method=="POST":

        uname=request.session["uname"]
        ctid=citizenreg.objects.get(uname=uname)
        sid=request.POST.get("station")
        ctype=request.POST.get("casetype")
        complaintt=request.POST.get("complaint")
        status='pending'
        c=complaint()
        c.ctid=ctid.id
        c.sid=sid
        c.complaint=complaintt
        c.ctype=ctype
        c.status=status
        c.save()
        if (ctype == "missing"):
            context = {}
            template =loader.get_template("missingcase.html")
            return HttpResponse(template.render(context, request))
        elif (ctype == "criminal"):
            context = {}
            template = loader.get_template("criminalcase.html")
            return HttpResponse(template.render(context, request))
        else:
            context = {}
            template = loader.get_template("theftcase.html")
            return HttpResponse(template.render(context, request))










    else:
        d=district.objects.all()
        context = {'dis':d}
        template = loader.get_template("addcomplaint.html")
        return HttpResponse(template.render(context, request))

def missing1(request):
    if request.method=="POST":
        name=request.POST.get("name")
        gen=request.POST.get("gen")
        age=request.POST.get("age")
        height=request.POST.get("height")
        color=request.POST.get("color")
        imarks=request.POST.get("imarks")
        mdate=request.POST.get("mdate")
        photo=request.FILES["photo"]
        rem=request.POST.get("remarks")
        m=missing()
        m.name=name
        m.gender=gen
        m.age=age
        m.height=height
        m.color=color
        m.imarks=imarks
        m.mdate=mdate
        m.photo=photo
        m.remarks=rem
        id=complaint.objects.raw("select max(id) as id from citizen_complaint")
        for i in id:
            cid=i.id
        m.cid=cid
        m.save()
        return HttpResponse("<script>alert('Missing case Registred successfully');window.location='/complaint';</script>")









    else:
        context = {}
        template = loader.get_template("missingcase.html")
        return HttpResponse(template.render(context, request))
def theft1(request):
    if request.method=="POST":
        id = complaint.objects.raw("select max(id) as id from citizen_complaint")
        for i in id:
            cid = i.id
        date=request.POST.get("date")
        object = request.POST.get("object")
        model = request.POST.get("model")
        quantity = request.POST.get("quantity")
        identificationte = request.POST.get("identification")
        remarks=request.POST.get("remarks")
        file=request.FILES["photo"]
        t=theft()
        t.cid=cid
        t.remarks=remarks
        t.photo=file
        t.date=date
        t.object=object
        t.model=model
        t.quantity=quantity
        t.identification=identificationte
        t.save()
        return HttpResponse("<script>alert('Theft case Registred successfully');window.location='/complaint';</script>")




    else:
        context = {}
        template = loader.get_template("theftcase.html")
        return HttpResponse(template.render(context, request))

def criminal1(request):
    if request.method=="POST":
        id = complaint.objects.raw("select max(id) as id from citizen_complaint")
        for i in id:
            cid = i.id
        date=request.POST.get("date")
        cname=request.POST.get("cname")
        gender=request.POST.get("gen")
        age=request.POST.get("age")
        address=request.POST.get("address")
        cnum=request.POST.get("cnum")
        remarks=request.POST.get("remarks")
        c=criminal()
        c.date=date
        c.cname=cname
        c.age=age
        c.gender=gender
        c.address=address
        c.contact=cnum
        c.remarks=remarks
        c.cid=cid
        c.save()
        return HttpResponse("<script>alert('Criminal case Registred successfully');window.location='/complaint';</script>")





    else:
        context = {}
        template = loader.get_template("criminalcase.html")
        return HttpResponse(template.render(context, request))
def citizenreg1(request):
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
        s=citizenreg()
        s.name=name
        s.email=email
        s.phone=phone
        s.hname=hname
        s.street=street
        s.city=city
        s.state=state
        s.pin=pin
        s.country=country
        s.uname=uname
        s.pwd=pwd
        s.status='pending'
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='citizen'
        l.save()
        s.save()

        return HttpResponse("<script>alert('Register successfully');window.location='/citizenreg';</script>")

    else:
        context={}
        template=loader.get_template("citizenreg.html")
        return HttpResponse(template.render(context,request))
def sortdistrict(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        did = request.GET.get('q')
        l = circle.objects.filter(disid=did).values()
        return JsonResponse(list(l), safe=False)

def sortcircle(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        did = request.GET.get('q')
        l = station.objects.filter(cid=did).values()
        return JsonResponse(list(l), safe=False)

def citizenviewstatus(request):
    uname=request.session["uname"]
    id=citizenreg.objects.get(uname=uname)
    c=complaint.objects.raw("select citizen_complaint.id,citizen_complaint.ctype,citizen_complaint.complaint,citizen_citizenreg.name,station_assigncase.status,station_assigncase.cremarks from citizen_citizenreg,citizen_complaint,station_assigncase,admin_station where citizen_complaint.id=station_assigncase.cmpid and citizen_complaint.ctid=citizen_citizenreg.id and  citizen_complaint.status='complete' and citizen_citizenreg.id=%s",[id.id])
    context={'key':c}
    template=loader.get_template("citizenviewstatus.html")
    return HttpResponse(template.render(context,request))
def searchlawer(request,id):
    l=lawyerreg.objects.filter(status='approve')
    request.session["cmpid"]=id
    context={'key':l}
    template = loader.get_template("searchlawer.html")
    return HttpResponse(template.render(context, request))

def selectlawer(request,id):
    lid=lawyerreg.objects.get(id=id)
    cmpid=request.session["cmpid"]
    l=selectedlawer()
    l.cmpid=cmpid
    l.lid=lid.id
    l.save()
    c=complaint.objects.get(id=cmpid)
    c.status="register"
    c.save()

    return HttpResponse("<script>alert('Complaint Send To Lawyer successfully');window.location='/citizenhome';</script>")


def citizenchangepass(request):
    if request.method=="POST":
        uname=request.session["uname"]
        opwd=request.POST.get("opwd")
        npwd=request.POST.get("npwd")
        l=login.objects.raw("SELECT * from admin_login where uname=%s and pwd=%s",[uname,opwd])
        if not l:
            return HttpResponse("<script>alert('Invalid Password');window.location='/citizenchangepass';</script>")
        else:
            l=login.objects.get(uname=uname,pwd=opwd)
            l.pwd=npwd
            l.save()
            c=citizenreg.objects.get(uname=uname)
            c.pwd=npwd
            c.save()
            return HttpResponse("<script>alert('Password Changed Successfully');window.location='/citizenchangepass';</script>")



    else:
        uname=request.session["uname"]
        context = {'key': uname}
        template = loader.get_template("citizenchangepass.html")
        return HttpResponse(template.render(context, request))