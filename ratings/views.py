from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect 
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Review, Customer,Record
from .forms import reviewForm

def showproduct(request):
    productlist = Product.objects.all()
    specific = Product.objects.get(serial_number=102)
    reviewList = Review.objects.all()
    return render(
        request, 'pdetails.html', {
            'productList': productlist,
            'specific': specific,
            'review': reviewList,
            'one':'1','two':'2','three':'3','four':'4','five':'5','good':'good','bad':'bad','neutral':'neutral',
        })
    
def showAboutInfo(request):
    return render(request, 'about.html')


def showComputer(request):
    return render(request, 'computer.html')


def showContactInfo(request):
    return render(request, 'contact.html')


def showIndex(request):
    return render(request, 'index.html')


def showLaptop(request):
    productlist = Product.objects.all()
    dictionary={'productlist':productlist}
    return render(request, 'laptop.html',dictionary)


def showHomePage(request):
    return render(request, 'home.html')

def hello(request):
    return render(request, 'hello.html')


def loginUser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.success(request,"Login error.Try again")
            return redirect("login")
    
    else:
        return render(request,'loginForm.html')

def logOutUser(request):    
    logout(request)
    messages.success(request,"Logged out")
    return redirect("homepage")

def registerUser(request):    
    if request.method=="POST":
        form=UserCreationForm(request.POST)   
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect("homepage")
    else:
        form=UserCreationForm()  
        return render(request, 'registrationForm.html',{"form":form})
     
def reviewAdd(request):  
    submitted=False
    if request.method=="POST":
        form=reviewForm(request.POST)
        if form.is_valid():
           
            reviewSTR=form.cleaned_data["review"]
            import pickle
            model = pickle.load(open("Web\static\model.sav", "rb"))
            hashvectorizer = pickle.load(open("Web\static\hashvectorizer.sav", "rb"))
            review=[reviewSTR]
            review=hashvectorizer.transform(review)
            prediction=model.predict(review)
            if prediction == 1:
               sentiment="good"
            elif prediction == 0:
                sentiment="neutral"
            else:
                sentiment="bad"
            data = Review()
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.product= form.cleaned_data['product']
            data.sentiment=sentiment
            data.customer=form.cleaned_data['customer']
            data.save()
            return  HttpResponseRedirect('/web/review?submitted=True')
    else:   
        form=reviewForm    
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'reviewForm.html',{"form":form,"submitted":submitted})  

def checkout(request):  
    return render(request, 'checkout_page.html')

def gotoPro(request):  
    data = Record()
    data.customer=request.user.username
    data.save()
    return render(request, 'checkout_page.html')