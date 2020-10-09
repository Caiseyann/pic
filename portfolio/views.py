# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image

# Create your views here.



# displaying different photo categories
def photo_category(request):
    date = dt.date.today()## current date
    portfolio = Image.objects.all
    return render(request, 'all-folios/category.html', {"date": date, "portfolio": portfolio})


def contact(request):
    date = dt.date.today()
    return render(request, 'all-folios/contact.html', {"date": date,})


def about(request):
    date = dt.date.today()
    return render(request, 'all-folios/about.html', {"date": date,})


## view function that will handle the logic for displaying the search results
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"


        ## render a HTML template and pass in the list of items found and the search_term.
        return render(request, 'all-folios/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request,'all-folios/search.html',{"message":message})
