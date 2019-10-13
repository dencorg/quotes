from django.shortcuts import render, get_object_or_404
from .models import Quote

def home(request):
    quotes = Quote.objects.all().order_by('is_draft')

    return render(request, 'main/index.html', {'quotes':quotes})

def single_quote(request, id):
    quote = get_object_or_404(Quote, pk=id)

    return render(request, 'main/single.html', {'quote':quote})
