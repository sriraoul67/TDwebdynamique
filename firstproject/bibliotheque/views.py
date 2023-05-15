from django.shortcuts import render
from .forms import LivreForm
from .models import models

def index(request):
    return render(request, 'firstproject/index.html')

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            return render(request,"/bibliotheque/affiche.html",{"livre": livre})
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else:
        form = LivreForm()
        return render(request,"bibliotheque/ajout.html",{"form": form})
