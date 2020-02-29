from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, BookOrder, Cart

# Create your views here.

def index(request):
  return render(request, 'template.html')

def books_list(request):
  books = Book.object.all()
  return render(request, 'base.html', {'books': books})

def book_detail(request, pk):
  book = get_object_or_404(Book, pk=pk)
  return render(request, 'store/detail.html', {'book': book})
  
def cart(request):
  if request.user.is_authenticated():
    cart = Cart.objects.filter(user=request.user.id, active=True)
    orders = BookOrder.objects.filter(cart=cart)
    total = 0
    count = 0
    for order in orders:
      total += (order.book.price * order.quantity)
      count += order.quantity
    return render(request, 'store/cart.html', {'cart': orders, 'total': total, 'count': count,})
  else:
    return redirect('index')