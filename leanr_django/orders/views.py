from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.models import Cart

# Create your views here.


def OrderCreate(request):
    user = request.user
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
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})
