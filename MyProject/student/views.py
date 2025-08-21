from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'student/index.html')



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
    obj=Item.objects.all()
    return render(request,'student/notes.html',{'obj':obj})

def batches(request):
    obj=Item1.objects.all()
    return render(request,'student/batches.html',{'obj':obj})

def softwarekit(request):
    x=mysoftware.objects.all().order_by('id')
    md={"sdata":x}
    return render(request,'student/softwarekit.html',md)

def tasks(request):
    return render(request,'student/tasks.html')

def uprofile(request):
    return render(request,'student/uprofile.html')



def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Process user message and generate response
        # Save user message to database
        Message.objects.create(user=request.user.userprofile, content=user_message)
        # Dummy response for demonstration
        bot_response = "Hello! How can I help you today?"
        return JsonResponse({'response': bot_response})
    else:
        return render(request, 'student/uprofile.html')

import spacy

nlp = spacy.load("en_core_web_sm")

def process_message(message):
    doc = nlp(message)
    # Process the parsed message
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
import requests

def fetch_medical_info(query):
    url = "https://api.example.com/medical-info"
    params = {"query": query, "apikey": "your_api_key"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Process the response data
        return data
    else:
        return None


# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
import spacy

nlp = spacy.load("en_core_web_sm")


# Dummy function to simulate processing user messages and generating responses
def process_message(message):
    # Example: Extract named entities from the message
    doc = nlp(message)
    entities = [ent.text for ent in doc.ents]
    return entities


def chat_view(request):
    if request.method == 'POST':
        # Get user message from the request
        user_message = request.POST.get('message')

        # Process user message
        processed_message = process_message(user_message)

        # Dummy response for demonstration
        bot_response = "Processed entities: " + ", ".join(processed_message)

        # Return response as JSON
        return JsonResponse({'response': bot_response})
    else:
        # Render the chat interface template
        return render(request, 'student/uprofile.html')
