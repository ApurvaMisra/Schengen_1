
from __future__ import division
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Target
from .models import TargetForm
from .models import ProbesForm
from .models import *
from .atlas_request_creation import atlas_api_call
from .atlas_request_stop import atlas_api_stop_call
from .atlas_request_fetch import atlas_api_result_call
from .forms import DateForm
from . import atlas_request_creation
from .models import Probes
from .models import Specification
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.forms import ModelForm
import datetime

from datetime import timedelta


def index(request):
    return render(request,'measurement/index.html')


def startf(request):


    if request.method == "POST":
        form = SpecificationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/measurement/probe')
    else:
        form = SpecificationForm()

    return render(request, 'measurement/startf.html', {'form': form})


def probefill(request):



    if request.method == "POST":
        form = ProbesForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/measurement/target')
    else:
        form = ProbesForm()

    return render(request, 'measurement/probefill.html', {'form': form})

def targetfill(request):
    if request.method == "POST":
        form = TargetForm(request.POST)

        if form.is_valid():
            form.save()
            msm=atlas_api_call()
            #return HttpResponseRedirect('http://127.0.0.1:8000/measurement/create')
            #context={'data':form.cleaned_data}
            #context = {'data': msm}
            q = Target.objects.all().last()
            q.msm_id=int(msm['measurements'][0])
            q.save()
            context = {'data': int(msm['measurements'][0])}
            return render(request, 'measurement/create.html', context)
    else:
        form = TargetForm()

    return render(request, 'measurement/targetfill.html', {'form': form})






def create(request):

    return HttpResponse('<h1>Measurement created</h1>')


def currenth(request):
    all_target=Target.objects.all()
    context={'all_target':all_target}
    return render(request,'measurement/currenth.html',context)


def option(request, msm_idvar):
    all_target=Target.objects.get(msm_id=msm_idvar)
    context={'all_target':all_target}
    return render(request,'measurement/option.html',context)


def stop(request,msm_idvar):

    atlas_api_stop_call(msm_idvar)
    q=Target.objects.get(msm_id=msm_idvar)
    q.status='stopped'
    q.save()
    return HttpResponse('<h1>Measurement stopped</h1>')




def result(request,msm_idvar):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            stop_date = form.cleaned_data['stop_date']
            countr=form.cleaned_data['country']
            #atlas_api_result_call(msm_idvar,start_date,stop_date,countr)
            des=Target.objects.get(msm_id=msm_idvar)
            desc=des.description
            rel=int(filter(str.isdigit, str(desc)))
            desc=desc.replace(" ","")
            desc=str(desc)
            rel="Relation"+str(rel)
            list1=[]
            m=1
            startins=start_date
            print startins
            while(True):
                date_min1=datetime.datetime.combine(startins, datetime.time.min)
                date_max1 = datetime.datetime.combine(startins, datetime.time.max)
                q1 = eval(desc).objects.filter(timestamp__range=[date_min1, date_max1])
                b=Countries.objects.get(country=countr)
                q2=q1.filter(countries=int(b.id))
                print q1.count()
                print q2.count()
                while(q2.count()==0):
                    startins = startins + timedelta(days=1)
                    date_min1 = datetime.datetime.combine(startins, datetime.time.min)
                    date_max1 = datetime.datetime.combine(startins, datetime.time.max)
                    q1 = eval(desc).objects.filter(timestamp__range=[date_min1, date_max1])
                    b = Countries.objects.get(country=countr)
                    q2 = q1.filter(countries=int(b.id))

                ratio=(q2.count()/q1.count())
                list1.append([m,ratio])
                m=m+1
                startins=startins+timedelta(days=3)
                if(startins>stop_date):
                    break

            context = {'reading': list1}
            #q1=eval(desc).objects.filter(timestamp__contains=datetime.date()
            return render(request, 'measurement/graph.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DateForm()

    return render(request, 'measurement/result.html', {'form': form})


