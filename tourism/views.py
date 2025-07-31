from django.shortcuts import render, get_object_or_404
from .models import Village

def village_list(request):
    villages = Village.objects.all()
    return render(request, 'tourism/village_list.html', {'villages': villages})

def village_detail(request, pk):
    village = get_object_or_404(Village, pk=pk)
    return render(request, 'tourism/village_detail.html', {'village': village})
