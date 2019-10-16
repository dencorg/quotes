from django.shortcuts import render, get_object_or_404
from .models import Quote

import random

def home(request):

    query = request.GET.get('q', None)

    if query:
        quotes = Quote.objects.filter(text__contains=query).order_by('is_draft')
    else:
        quotes = Quote.objects.all().order_by('is_draft')

    return render(request, 'main/index.html', {'quotes':quotes})

def single_quote(request, id):
    quote = get_object_or_404(Quote, pk=id)

    return render(request, 'main/single.html', {'quote':quote})

def random_quote(request):
    quotes = Quote.objects.filter(is_draft=False)
    random_quote = random.choice(quotes)

    return render(request, 'main/single.html', {'quote':random_quote})
