from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    sdata=slider.objects.all().order_by('-id')[0:3]
    nbdata = newbatches.objects.all().order_by('-id')[0:3]
    mydict={"sd":sdata,"nbdata":nbdata}


    return render(request,'user/index.html',mydict)
def about(request):
    return render(request,'user/about.html')
def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('mobile')
        c=request.POST.get('email')
        d=request.POST.get('msg')
        contactus(name=a,mobile=b,email=c,message=d).save()
        return HttpResponse("<script>alert('Thanks for contacting with us..');location.href='/user/contact/'</script>")

    return render(request,'user/contact.html')
def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        fu=request.FILES.get('fu')
        pyear = request.POST.get('pyear')
        x=registration.objects.filter(email=email).count()
        if x==0:
            registration(name=name,email=email,mobile=mobile,passwd=passwd,college=college,course=course,profile=fu,status='Pending',batch='Free').save()

            return HttpResponse("<script>alert('You are  Registered successfully');location.href='/user/registration/'</script")
        else:
            return HttpResponse("<script>alert('You are  Registered successfully');location.href='/user/registration/'</script>")

    return render(request,'user/signup.html')
def studentlogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=registration.objects.filter(passwd=passwd,email=email).count()

        if x==1:
            request.session['user']=email
            y=registration.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)
            return HttpResponse("<script>location.href='/student/index/'</script>")
        else:
            return HttpResponse("<script>alert('your username or password incorrect');location.href='/user/login/'</script>")
    return render(request,'user/studentlogin.html')
def feedback(request):
    return render(request,'user/feedback.html')
def newbatchess(request):
    batchdata=newbatches.objects.all().order_by('-id')
    md={"bdata":batchdata}
    return render(request,'user/newbatches.html',md)
def ourfacility(request):
    return render(request,'user/ourfacility.html')

def successstories(request):
    collegedata=college.objects.all().order_by('-id')
    sdata=session_year.objects.all().order_by('-id')
    pdata= placement.objects.all().order_by('-id')

    md={"cdata":collegedata,"sdata":sdata,"pdata":pdata}
    return render(request,'user/successstories.html',md)



