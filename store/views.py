from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Cart, Category

# Create your views here.


def index(request):
    return render(request, 'template.html')


def store(request):
    books = Book.objects.order_by('-created_at')
    return render(request, 'base.html', {'books': books})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'store/detail.html', {'book': book})


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category = Book.objects.filter(category=category)
    return render(request, 'store/books_by_tag.html', {'books': books_for_category, 'category': category})


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
