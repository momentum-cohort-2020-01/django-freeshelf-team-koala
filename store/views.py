from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Cart, Category

# Create your views here.


def homepage(request):
    books = Book.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    return render(request, 'store/index.html', {'books': books, 'category': category, 'authors': author})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'store/detail.html', {'book': book})


def author(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'store/author.html', {'author': author, 'pk': pk})


def store(request):
    books = Book.objects.order_by('-created_at')
    return render(request, 'base.html', {'books': books})


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category = Book.objects.filter(category=category)
    return render(request, 'store/category.html', {'books': books_for_category, 'category': category})


def index(request):
    return render(request, 'index.html')

# def cart(request):
#   if request.user.is_authenticated():
#     cart = Cart.objects.filter(user=request.user.id, active=True)
#
#     total = 0
#     count = 0
#     for order in orders:
#       total += (order.book.price * order.quantity)
#       count += order.quantity
#     return render(request, 'store/cart.html', {'cart': orders, 'total': total, 'count': count,})
#   else:
#     return redirect('index')
