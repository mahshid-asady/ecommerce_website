from django.shortcuts import render, redirect

from eshop_cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .task import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # clear the cart
                cart.clear()
                order_created(order.id)
                request.session['order_id'] = order.id
                # redirect to the payment
                return redirect('process')
            else:
                form = OrderCreateForm()
                return render(request, 'create_order.html', {'cart': cart, 'form': form})
