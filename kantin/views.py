from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Makanan

# Create your views here.
def home(request):
    searchMakanan = request.GET.get('nama')
    if searchMakanan:
        makanan = Makanan.objects.filter(nama_icontains=searchMakanan)
    else:
        makanan = Makanan.objects.all()
    return render(request, "home.html", {'search': searchMakanan, 'makanans': makanan})

def makanan(request, makanan_id):
    makanan = get_object_or_404(Makanan, pk=makanan_id)
    return HttpResponse("Makanan")