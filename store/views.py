from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def books_list(request):
  books = Book.object.all()
  return render(request, 'base.html', {'books': books})

def book_detail(request, pk):
  book = get_object_or_404(pk=pk)
  return render(request, 'store/detail.html', {'book': book} )