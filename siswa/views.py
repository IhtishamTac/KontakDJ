from django.shortcuts import render
from .models import siswa

# Create your views here.

def siswa(request):
    return render(request, "page/page_siswa/data_siswa.html")
    