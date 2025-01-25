from django.shortcuts import render
from .models import Word  # Assuming there is a Word model in models.py

def index(request):
    words = Word.objects.all()  # Fetch all words from the database
    return render(request, 'learning/learn.html', {'words': words})  # Render the main learning page with words

def course_detail(request, course_id):
    # Logic to retrieve course details based on course_id
    # For now, we will just render a placeholder template
    return render(request, 'learning/course_detail.html', {'course_id': course_id})
