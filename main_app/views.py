from django.shortcuts import render, redirect
from .models import Choreographer, Sheet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sheet_index(request):
    sheets = Sheet.objects.all()
    return render(request, 'sheets/index.html', {'sheets': sheets})

def sheet_detail(request, sheet_id):
    sheet = Sheet.objects.get(id=sheet_id)
    return render(request, 'sheets/detail.html', {'sheet': sheet})

class SheetCreate(CreateView):
    model = Sheet
    fields = '__all__'
    success_url = '/stepsheets/'

class SheetUpdate(UpdateView):
    model = Sheet
    fields = '__all__'

class SheetDelete(DeleteView):
    model = Sheet
    success_url = '/stepsheets/'

class ChoreoList(ListView):
    model = Choreographer
    template_name = 'choreographers/index.html'

class ChoreoDetail(DetailView):
    model = Choreographer
    template_name = 'choreographers/detail.html'

class ChoreoCreate(CreateView):
    model = Choreographer
    fields = '__all__'

def assoc_choreo(request, sheet_id, choreo_id):
    Sheet.objects.get(id=sheet_id).choreo.add(choreo_id)
    return redirect('detail', sheet_id=sheet_id)
