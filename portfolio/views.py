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
