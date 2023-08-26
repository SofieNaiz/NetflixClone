from django.shortcuts import render, redirect
from .models import *

def dashboard(request):
    films = film.objects.all()
    movies = []
    series = []
    for i in films:
        if i.filmType == "movies":
            movies.append(i)
        else:
            series.append(i)
                
    return render(request, "dashboard/dashboard.html", context={"movies": movies, "series": series})

def sign_out(request):
    request.session.clear()
    return redirect("/")

def movies(request):
    films = film.objects.all()
    movies = []
    for i in films:
        if i.filmType == "movies":
            movies.append(i)

    return render(request, "dashboard/movies.html", context={"movies": movies})

def series(request):
    films = film.objects.all()
    series = []
    for i in films:
        if i.filmType == "series":
            series.append(i)
            
    return render(request, "dashboard/series.html", context={"series": series})

def search_file(request):
    srch = request.GET['search_name'].lower()
    films = film.objects.all()
   
    
    #filter out the requested searches
    results = []
    for i in films:
        s = str(i.name).lower()
        print("..>>>>", s)
        if s.__contains__(srch):
            results.append(i)
        
    #return the results
    return render(request, "dashboard/search.html",
                  context={"result": "found" if len(results) > 0 else "none",
                      "zz": results if len(results) > 0 else "No record found!"})