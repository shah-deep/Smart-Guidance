from django.shortcuts import render, redirect
from .models import Topic

# Create your views here.

def home(request):
    # print(request)
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request,'base/index.html', context)

def topic_chemistry(request):
    topics = Topic.objects.filter(subject = "chemistry")
    context = {'topics':topics}
    return render(request,'base/chemistry.html', context)


def topic_flora(request):
    topics = Topic.objects.filter(subject = "flora")
    context = {'topics':topics}
    return render(request,'base/flora.html', context)

def topic_fauna(request):
    topics = Topic.objects.filter(subject = "fauna")
    context = {'topics':topics}
    return render(request,'base/fauna.html', context)


def topic_machinery(request):
    topics = Topic.objects.filter(subject = "machinery")
    context = {'topics':topics}
    return render(request,'base/machinery.html', context)

def topic_default(request):
    topics = Topic.objects.filter(subject = "default")
    context = {'topics':topics}
    return render(request,'base/default.html', context)

def topic_biology(request):
    topics = Topic.objects.filter(subject = "biology")
    context = {'topics':topics}
    return render(request,'base/biology.html', context)

def topic_astronomy(request):
    topics = Topic.objects.filter(subject = "astronomy")
    context = {'topics':topics}
    return render(request,'base/astronomy.html', context)

def topic_part(request, slug):
    topic = Topic.objects.get(slug = slug)
    context = {'topic':topic}
    return render(request,'base/topic.html', context)
