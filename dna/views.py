from django.shortcuts import render
# from dna.forms import ProfileForm

# Create your views here.
from dna.models import Dna


def dna(request):
    dna = Dna.objects.all()
    data = {"dna": dna}
    return render(request, "dna.html", data)




