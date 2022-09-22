from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_watchlist(request):
    data_watchlist = MyWatchList.objects.all()
    watch_many = is_watch_many(data_watchlist)
    context = {
        'watchlist': data_watchlist,
        'is_watch_many': watch_many,
        'nama': "Erlangga Ahmad Khadafi",
        'npm': '2106750894',
    }
    return render(request, "mywatchlist.html", context)

def is_watch_many(movies):
    count_watched = 0
    for movie in movies:
        if movie.watched == True:
            count_watched += 1
    print(count_watched >= (len(movies) - count_watched))
    return count_watched >= (len(movies) - count_watched)