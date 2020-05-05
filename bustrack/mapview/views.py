from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.http import HttpResponse
from . models import Loc,Rawdata

def homepage(request):
	locs=Loc.objects.all()

	return render(request,'homepage.html',{"locs":locs}) 
def index(request):
	locs=Loc.objects.all()

	return render(request,'index.html',{"locs":locs}) 	

def detail(request, bno):
    
    locs=Loc.objects.all();raw=Rawdata.objects.all()
    try:
        bus=Loc.objects.get(bno=bno);curRaw=Rawdata.objects.filter(bno=bno).last();
    except Loc.DoesNotExist:
        raise Http404("Bus does not exist")
    return render(request, 'bus-detail.html', { 'bno':bno, 'raw':raw, 'bus' : bus, 'locs' : locs, 'curRaw':curRaw})

def info(request,bno):
	data=Rawdata.objects.filter(bno=bno).last();
	curRaw={
	'lat':data.lat,
	'lon':data.lon,
	}
	return JsonResponse(curRaw)

def alerts(request):
	locs=Loc.objects.all()

	return render(request,'alerts.html',{"locs":locs}) 
