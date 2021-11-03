from django.shortcuts import render

def main_rest(request) :
    return render(request, "search/search_restaurant.html")

def main_tour(request) :
    return render(request, "search/search_tourspots.html")


# Create your views here.
