from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from .models import login,designation,circle,district,station
from citizen.models import citizenreg,complaint,missing,criminal,theft
from lawer.models import lawyerreg
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def adminhome(request):
    return render(request, 'adminhome.html')
def login1(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        if(login.objects.filter(uname=uname,pwd=pwd)):
            li=login.objects.filter(uname=uname,pwd=pwd)
            for i in li:
                if(i.utype == "admin"):
                    context = {}
                    template = loader.get_template("adminhome.html")
                    return HttpResponse(template.render(context, request))

                elif(i.utype == "citizen"):
                    u=citizenreg.objects.get(uname=uname)
                    if(u.status=="pending"):
                        return HttpResponse("<script>alert('NoT Approved by admin');window.location='/login';</script>")
                    else:
                        request.session["uname"]=uname
                        context = {}
                        template = loader.get_template("citizenhome.html")
                        return HttpResponse(template.render(context, request))
                elif (i.utype == "lawyer"):
                    u = lawyerreg.objects.get(uname=uname)
                    if (u.status == "pending"):
                        return HttpResponse("<script>alert('NoT Approved by admin');window.location='/login';</script>")
                    else:
                        request.session["uname"] = uname
                        context = {}
                        template = loader.get_template("lawerhome.html")
                        return HttpResponse(template.render(context,request))
                elif (i.utype == "officer"):
                    request.session["uname"] = uname

                    context = {}
                    template = loader.get_template("officerhome.html")
                    return HttpResponse(template.render(context, request))
                elif (i.utype == "station"):
                    request.session["uname"] = uname

                    context = {}
                    template = loader.get_template("stationhome.html")
                    return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("<script>alert('invalid uname or pwd');window.location='/login';</script>")
    else:

        context = {}
        template = loader.get_template("login.html")
        return HttpResponse(template.render(context, request))

def designation1(request):
    if request.method == "POST":
        dname = request.POST.get("dname")
        s=designation()
        s.dname=dname
        s.save()
        return HttpResponse("<script>alert('Designation Added successfully');window.location='/designation';</script>")

    else:
        context = {}
        template = loader.get_template("AddDesignation.html")
        return HttpResponse(template.render(context, request))


def district1(request):
    if request.method == "POST":
        disname = request.POST.get("disname")
        s = district()
        s.disname = disname
        s.save()
        return HttpResponse("<script>alert('District Added successfully');window.location='/district';</script>")

    else:
        context = {}
        template = loader.get_template("Adddistrict.html")
        return HttpResponse(template.render(context, request))

def circle1(request):
    if request.method == "POST":
        circlename = request.POST.get("cname")
        did=request.POST.get("dname")
        did1=district.objects.get(id=did)
        s = circle()
        s.circlename = circlename
        s.disid=did1.id
        s.save()
        return HttpResponse("<script>alert('Circle Added successfully');window.location='/circle';</script>")

    else:
        d=district.objects.all()
        context = {'key':d}
        template = loader.get_template("addcircle.html")
        return HttpResponse(template.render(context, request))
def station1(request):
    if request.method=="POST":
        sname=request.POST.get("sname")
        scode=request.POST.get("scode")
        enum=request.POST.get("enum")
        cnum = request.POST.get("cnum")
        uname = request.POST.get("uname")
        pwd=request.POST.get("pwd")
        cid=request.POST.get("cname")
        cid1=circle.objects.get(id=cid)
        s=station()
        s.sname=sname
        s.scode=scode
        s.enum=enum
        s.cnum=cnum
        s.uname=uname
        s.pwd=pwd
        s.cid=cid1.id
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='station'
        l.save()
        s.save()
        return HttpResponse("<script>alert('Station Added successfully');window.location='/station';</script>")

    else:
        c=circle.objects.all()
        context = {'key':c}
        template = loader.get_template("addstation.html")
        return HttpResponse(template.render(context, request))

def viewdesignation1(request):
    m =designation.objects.all()
    context = {'key':m}
    template = loader.get_template("viewdesignation.html")
    return HttpResponse(template.render(context, request))
def desigdelete1(request,id):
    d=designation.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewdesig';</script>")


def desigedit1(request,id):
    s=designation.objects.get(id=id)

    context={'key':s}
    template = loader.get_template("updatedesig.html")
    return HttpResponse(template.render(context, request))
def desigupdate1(request,id):

    s=designation.objects.get(id=id)
    dname = request.POST.get("dname")
    s.dname=dname
    s.save()
    return HttpResponse("<script>alert('updated successfully');window.location='/viewdesig/';</script>")


def viewdistrict2(request):
    m =district.objects.all()
    context = {'key':m}
    template = loader.get_template("viewdistrict.html")
    return HttpResponse(template.render(context, request))
def disdelete2(request,id):
    d = district.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewdis';</script>")
def disedit2(request,id):
    s = district.objects.get(id=id)
    context = {'key': s}
    template = loader.get_template("updatedis.html")
    return HttpResponse(template.render(context, request))
def disupdate2(request,id):
    s=district.objects.get(id=id)
    disname = request.POST.get("disname")
    s.disname=disname
    s.save()
    return HttpResponse("<script>alert('updated successfully');window.location='/viewdis/';</script>")
def viewcitizen(request):
    m =citizenreg.objects.filter(status='pending')
    context = {'key':m}
    template = loader.get_template("viewcitizen.html")
    return HttpResponse(template.render(context, request))
def approvecitizen(request,id):
    r = citizenreg.objects.get(id=id)
    request.session["email"] = r.email
    r.status = 'approve'
    r.save()
    subject = 'You got an email from crime investigator'
    message = 'Your request accepted successfully!!!!Now you can access your account'
    email_from = settings.EMAIL_HOST_USER
    mailid = request.session["email"]
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('Approved successfully');window.location='/viewcitizen';</script>")
def rejectcitizen(request,id):
    r=citizenreg.objects.get(id=id)
    request.session["email"]=r.email
    r.status='reject'
    r.save()
    subject = 'You got an email from crime investigator'
    message = 'Your request has declined!!!!Check your request...'
    email_from = settings.EMAIL_HOST_USER
    mailid = request.session["email"]
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('Rejected successfully');window.location='/viewcitizen';</script>")
def viewlawer(request):
    m =lawyerreg.objects.filter(status='pending')
    context = {'key':m}
    template = loader.get_template("viewlawer.html")
    return HttpResponse(template.render(context, request))
def approvelawer(request,id):
    r=lawyerreg.objects.get(id=id)
    request.session["email"]=r.email
    r.status='approve'
    r.save()
    subject = 'You got an email from crime investigator'
    message = 'Your request accepted successfully!!!!Now you can access your account'
    email_from = settings.EMAIL_HOST_USER
    mailid = request.session["email"]
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('Approved successfully');window.location='/viewlawer';</script>")
def rejectlawer(request,id):
    r=lawyerreg.objects.get(id=id)
    request.session["email"]=r.email
    r.status='reject'
    r.save()
    subject = 'You got an email from crime investigator'
    message = 'Your request has declined!!!!Check your request...'
    email_from = settings.EMAIL_HOST_USER
    mailid = request.session["email"]
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('Rejected successfully');window.location='/viewlawer';</script>")
def viewcircle(request):
    m =circle.objects.all()
    context = {'key':m}
    template = loader.get_template("viewcircle.html")
    return HttpResponse(template.render(context, request))
def circledelete(request,id):
    d=circle.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewcircle';</script>")
def circleedit(request,id):
    s=circle.objects.get(id=id)

    context={'key':s}
    template = loader.get_template("updatecircle.html")
    return HttpResponse(template.render(context, request))
def circleupdate(request,id):

    s=circle.objects.get(id=id)

    circlename = request.POST.get("circlename")
    s.circlename=circlename
    s.save()
    return HttpResponse("<script>alert('updated successfully');window.location='/viewcircle';</script>")

def viewstation(request):
    m =station.objects.all()
    context = {'key':m}
    template = loader.get_template("viewstation.html")
    return HttpResponse(template.render(context, request))
def stationdelete(request,id):
    d=station.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewstation';</script>")
def stationedit(request,id):
    s=station.objects.get(id=id)

    context={'key':s}
    template = loader.get_template("updatestation.html")
    return HttpResponse(template.render(context, request))
def stationupdate(request,id):

    s=station.objects.get(id=id)
    ouname=s.uname
    sname = request.POST.get("sname")
    scode=request.POST.get("scode")
    enum=request.POST.get("enum")
    cnum=request.POST.get("cnum")

    s.sname=sname
    s.scode=scode
    s.enum=enum
    s.cnum=cnum

    s.save()

    return HttpResponse("<script>alert('updated successfully');window.location='/viewstation';</script>")

def viewlawer1(request,id):
    id=lawyerreg.objects.get(id=id)
    context={'key':id}
    template=loader.get_template("viewlawer1.html")
    return HttpResponse(template.render(context,request))

def verifycomplaint(request):
    c=complaint.objects.raw("SELECT * FROM citizen_complaint,citizen_citizenreg,admin_station where citizen_complaint.ctid=citizen_citizenreg.id and citizen_complaint.sid=admin_station.id and citizen_complaint.status='pending'")
    context={'key':c}
    template=loader.get_template("verifycomplaint.html")
    return HttpResponse(template.render(context,request))
def viewdetails(request,id):
    id1=complaint.objects.get(id=id)
    if(id1.ctype=="missing"):
        c=missing.objects.get(cid=id)
        context = {'key': c}
        template = loader.get_template("verifymissing.html")
        return HttpResponse(template.render(context, request))
    elif(id1.ctype=="criminal"):
        c=criminal.objects.get(cid=id)
        context = {'key': c}
        template = loader.get_template("verifycriminal.html")
        return HttpResponse(template.render(context, request))
    else:
        c = theft.objects.get(cid=id)
        context = {'key': c}
        template = loader.get_template("verifytheft.html")
        return HttpResponse(template.render(context, request))


def verifymissing(request,id):

    c=complaint.objects.get(id=id)
    c.status='verify'
    c.save()
    return HttpResponse("<script>alert('verified successfully');window.location='/verifycomplaint';</script>")
def verifycriminal(request,id):

    c=complaint.objects.get(id=id)
    c.status='verify'
    c.save()
    return HttpResponse("<script>alert('verified successfully');window.location='/verifycomplaint';</script>")
def verifytheft(request,id):

    c=complaint.objects.get(id=id)
    c.status='verify'
    c.save()
    return HttpResponse("<script>alert('verified successfully');window.location='/verifycomplaint';</script>")
def adminviewcasestatus(request):
    c=complaint.objects.raw("select citizen_complaint.*,citizen_citizenreg.name,citizen_citizenreg.email,citizen_citizenreg.phone,citizen_citizenreg.hname,citizen_citizenreg.street,citizen_citizenreg.city,citizen_citizenreg.state,citizen_citizenreg.pin,citizen_citizenreg.country,station_officer.officername,admin_station.sname from citizen_citizenreg,citizen_complaint,station_officer,station_assigncase,admin_station where citizen_citizenreg.id=citizen_complaint.ctid and station_officer.id=station_assigncase.offid and citizen_complaint.status='complete' and station_assigncase.cmpid=citizen_complaint.id and admin_station.id=citizen_complaint.sid")
    context = {'key': c}
    template = loader.get_template("adminviewcasestatus.html")
    return HttpResponse(template.render(context, request))
def adminviewmissing(request,id):
    id1=complaint.objects.get(id=id)
    ctype=id1.ctype
    if(ctype=="missing"):
        c = missing.objects.raw(
            "select citizen_missing.*,station_assigncase.* from citizen_missing,station_assigncase where citizen_missing.cid=station_assigncase.cmpid and citizen_missing.cid=%s",
            [id])
        context = {'key': c}
        template = loader.get_template("adminviewmissing.html")
        return HttpResponse(template.render(context, request))
    elif(ctype=="criminal"):
        c = criminal.objects.raw("select citizen_criminal.*,station_assigncase.* from citizen_criminal,station_assigncase where citizen_criminal.cid=station_assigncase.cmpid and citizen_criminal.cid=%s",[id])
        context = {'key': c}
        template = loader.get_template("adminviewcriminal.html")
        return HttpResponse(template.render(context, request))
    else:
        c = theft.objects.raw("select citizen_theft.*,station_assigncase.* from citizen_theft,station_assigncase where citizen_theft.cid=station_assigncase.cmpid and citizen_theft.cid=%s",[id])
        context = {'key': c}
        template = loader.get_template("adminviewtheft.html")
        return HttpResponse(template.render(context, request))
def npwd(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("npwd")
        l=login.objects.raw("SELECT * from admin_login WHERE uname=%s",[uname])
        if not l:
            return HttpResponse("<script>alert('invalid uname');window.location='/npwd';</script>")
        else:
            l=login.objects.get(uname=uname)
            l.pwd=pwd
            l.save()
            return HttpResponse("<script>alert('password reset');window.location='/login';</script>")




    else:
        context = {}
        template = loader.get_template("npwd.html")
        return HttpResponse(template.render(context, request))




