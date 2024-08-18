from django.shortcuts import render, redirect
from .models import Order
from catalog.models import Product
from django.contrib.auth.decorators import login_required
from decimal import Decimal

@login_required
def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        total_price = quantity * product.price
        Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )
        return redirect('order_confirmation')

    return render(request, 'orders/create_order.html', {'product': product})

