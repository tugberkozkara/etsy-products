from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
import requests
from bs4 import BeautifulSoup


def getSoup(inputURL):      # Get the soup once to use it while finding elements
    global soup     
    resp = requests.get(inputURL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(resp.status_code)

def getName():      # Find h1 tag with the exact class attr to get the name of the product
    name = soup.find("h1", class_="wt-text-body-03").string.strip()
    print(name)
    return name

def getImage():     # Find img tag with class attr, then get its 'src' attr
    image = soup.find("img", class_="wt-max-width-full")['src']
    print(image)
    return image

def getPrice():
    priceTag = soup.find("p", class_="wt-text-title-03")
    
    if priceTag.string == None:     # Check if price tag has another tag inside
        price = list(priceTag.children)[2].strip()
    else:
        price = priceTag.string.strip()
    
    print(price)
    return price

def homePage(request):      # Get the inserted URL extract needed elements, then save into DB
    try:
        if request.method == "POST":
            inputURL = request.POST['inputURL']
            getSoup(inputURL)
            ins = Product(name=getName(), img_url=getImage(), price=getPrice())
            ins.save()
            print("Product saved successfully!")
            messages.success(request, "Successfully saved!")
            return redirect("collection")
    except:
        print("A problem ocurred!")
        messages.error(request, "Invalid URL!")
        return redirect("homepage")
    return render(request, "homepage.html")


def collectionPage(request):        # Get all objects inside DB to list in Collection Page
    products = Product.objects.all()
    return render(request, "collection.html", {"products": products})

def productDetail(request, id):
    product = Product.objects.filter(id = id).first()
    return render(request, "detail.html", {"product": product})

def deleteProduct(request, id):
    product = Product.objects.filter(id = id).first()
    product.delete()
    return redirect("collection")