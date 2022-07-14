from distutils.log import error
from django.shortcuts import render, redirect
from .models import Choreographer, Sheet, Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sheet_index(request):
    sheets = Sheet.objects.all().order_by('-id')
    return render(request, 'sheets/index.html', {'sheets': sheets})

def sheet_detail(request, sheet_id):
    sheet = Sheet.objects.get(id=sheet_id)
    return render(request, 'sheets/detail.html', {'sheet': sheet})

class VideoCreate(LoginRequiredMixin, CreateView):
    model = Video
    fields = '__all__'
    success_url = '/stepsheets/'

    def form_valid(self, form):
        form.instance.url = self.request.POST.get('url').replace('watch?v=', 'embed/')
        form.instance.user = self.request.user
        return super().form_valid(form)

class SheetCreate(LoginRequiredMixin, CreateView):
    model = Sheet
    fields = '__all__'
    success_url = '/stepsheets/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SheetUpdate(LoginRequiredMixin, UpdateView):
    model = Sheet
    fields = '__all__'

class SheetDelete(LoginRequiredMixin, DeleteView):
    model = Sheet
    success_url = '/stepsheets/'

class ChoreoList(ListView):
    model = Choreographer
    template_name = 'choreographers/index.html'

class ChoreoDetail(DetailView):
    model = Choreographer
    template_name = 'choreographers/detail.html'

class ChoreoCreate(LoginRequiredMixin, CreateView):
    model = Choreographer
    fields = '__all__'
    success_url = '/choreographers/'

@login_required
def assoc_choreo(request, sheet_id, choreo_id):
    Sheet.objects.get(id=sheet_id).choreo.add(choreo_id)
    return redirect('detail', sheet_id=sheet_id)

@login_required
def assoc_video(request, sheet_id, video_id):
    Sheet.objects.get(id=sheet_id).video.add(video_id)
    return redirect('detail', sheet_id=sheet_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Standard User')
            user.groups.add(group)
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up. Please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class SearchResults(ListView):
    model = Sheet
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Sheet.objects.filter(Q(title__icontains=query)).order_by('title')