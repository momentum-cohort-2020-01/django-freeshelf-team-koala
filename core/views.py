from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def books_list(request):
  books = Book.object.all()
  # Link to Cheryl's HTML here
  return render(request, 'core/books_list.html', {'books': books})