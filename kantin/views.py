from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Makanan
from .models import Kantin

# Create your views here.
def home(request):
    searchMakanan = request.GET.get('nama')
    if searchMakanan:
        makanan = Makanan.objects.filter(nama__icontains=searchMakanan)
    else:
        makanan = Makanan.objects.all()
    return render(request, "home.html", {'search': searchMakanan, 'makanans': makanan})

def makanan(request, makanan_id):
    makanan = get_object_or_404(Makanan, pk=makanan_id)
    return render(request, "makanan.html", {"makanan": makanan})

def kantin(request, kantin_id):
    kantin = get_object_or_404(Kantin, pk=kantin_id)
    return HttpResponse(kantin)

def about(request):
    return render(request, "about.html")