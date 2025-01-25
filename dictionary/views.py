from django.shortcuts import render
from .models import Word

def index(request):
    return render(request, 'dictionary.html')

def word_detail(request, word):
    word_entry = Word.objects.get(name=word)
    return render(request, 'word_detail.html', {'word_entry': word_entry})
