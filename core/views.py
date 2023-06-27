from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import *

def home(request):
  if request.method == "POST":
    url = request.POST["url"]

    response_ = requests.get(url)
    scrap = BeautifulSoup(response_.text,"lxml")

    pd_name =  scrap.find_all("div",class_ = "_4rR01T")
    pd_img = scrap.find_all("img",class_ = "_396cs4")
    pd_price = scrap.find_all("div",class_ = "_30jeq3")
    pd_rating = scrap.find_all("div",class_ = "_3LWZlK")
    pd_details = scrap.find_all("a",class_ = "_1fQZEK")
    
    for name, img, price,rating,details in zip(pd_name, pd_img, pd_price,pd_rating,pd_details):
      data = ScrapingData(thumbnail=img['src'],title=name.get_text(),rating=rating.get_text(),price=price.get_text(),details="https://www.flipkart.com"+details['href'])
      data.save()
    return redirect('Home')
  
  scrap_data = ScrapingData.objects.order_by("-id") 
  return render(request,"core/index.html",locals())



def delete(request,id):
  data = ScrapingData.objects.get(id=id)
  data.delete()
  return redirect('Home')
  
  