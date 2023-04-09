from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SearchModel
from .forms import SearchModelForm

import folium #displaying maps of database data
import geocoder # process of converting addresses into geographical coordinates.

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = SearchModelForm(request.POST)
        request.POST.get
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = SearchModelForm()

    address = SearchModel.objects.all()

    location = geocoder.osm(address)
    lat = location.lat if location.lat!=None else 40
    long = location.lng if location.lng!=None else 35
    country = location.country

    if long == None or lat == None:
        address.delete()
        return HttpResponse('You address input is valid')

    #Create map object
    map = folium.Map(location=(40,35),zoom_start=2)

    # Add a marker on the map object
    folium.Marker([lat,long],tooltip='Click for more',popup=country).add_to(map)

    # represent html of map object
    map = map._repr_html_()
    return render(request,'index.html',context={
        'map':map,
        'form':form
    })