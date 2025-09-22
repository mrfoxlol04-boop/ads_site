# ads/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Advertisement

def home(request):
    advertisements_list = Advertisement.objects.all()
    paginator = Paginator(advertisements_list, 15)  # 15 объявлений на странице
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'ads/home.html', {'page_obj': page_obj})

def advertisement_detail(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'ads/advertisement_detail.html', {'advertisement': advertisement})

def about(request):
    return render(request, 'ads/about.html')