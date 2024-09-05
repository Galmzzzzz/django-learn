from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ArticlesForm()

    data = {
            'form': form,
       }

    return render(request, 'mews/mews.html', data)

def mews(request):
    mews = Articles.objects.all()
    return render(request, 'mews/read_mews.html', {'mews': mews})

