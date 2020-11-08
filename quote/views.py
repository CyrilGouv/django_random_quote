from django.http import HttpResponse
from django.shortcuts import render
from .models import Quote
import random

def quote_list(request) :
    count = Quote.objects.all().count()

    num_random = random.randint(1, count)

    quote = Quote.objects.get(id=num_random)

    context = {
        'quote': quote
    }

    return render(request, 'index.html', context)
