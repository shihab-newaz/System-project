from django.shortcuts import render
from django.http import HttpResponse
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import re
# Create your views here.
def test(request):
    return render(request,'hello.html',{'name':'shihab'})

def getPredictions(request):
    import pickle
    model = pickle.load(open("Web\static\model.sav", "rb"))
    hashvectorizer = pickle.load(open("Web\static\hashvectorizer.sav", "rb"))
    
    reviewSTR= str(request.GET['review'])
    review=[reviewSTR]
    review=hashvectorizer.transform(review)
    prediction=model.predict(review)
    if prediction == 1:
         return render(request, 'result.html', {'result':'positive','review':reviewSTR})
    elif prediction == 0:
        return render(request, 'result.html', {'result':'neutral','review':reviewSTR})
    else:
        return render(request, 'result.html', {'result':'negative','review':reviewSTR})
    
def showHome(request):
    return render(request,'home.html')