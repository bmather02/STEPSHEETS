from django.shortcuts import render
from .models import Sheet
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sheet_index(request):
    sheets = Sheet.objects.all()
    return render(request, 'sheets/index.html', {'sheets': sheets})
