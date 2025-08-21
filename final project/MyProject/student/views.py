from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'student/index.html')

def batches(request):
    return render(request,'student/batches.html')

def lectures(request):
    cdata=category.objects.all().order_by('-id')
    md={"cdata":cdata}
    return render(request,'student/lectures.html',md)

def lecturesvideo(request):
    batchid=request.session.get('batchid')
    cid=request.GET.get('cid')
    vdata=mylectures.objects.filter(video_category=cid,video_batch=batchid)
    md={"vdata":vdata}
    return render(request,'student/lecturesvideo.html',md)



def liveclasses(request):
    return render(request,'student/liveclasses.html')

def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['userpic']
        del request.session['username']
        return HttpResponse("<script>location.href='/user/index/'</script>")
    return render(request,'student/logout.html')

def notes(request):
    return render(request,'student/notes.html')

def softwarekit(request):
    x=mysoftware.objects.all().order_by('id')
    md={"sdata":x}
    return render(request,'student/softwarekit.html',md)

def tasks(request):
    return render(request,'student/tasks.html')

def uprofile(request):
    return render(request,'student/uprofile.html')