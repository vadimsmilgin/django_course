from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from cart.models import Cart
from shop.models import Item
from cart.forms import CartAddProductForm

# Create your views here.

    @require_POST
    def CartAdd(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Item, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.changed_data
            cart.add(product= product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart:CartDetail')

    def CartRemove(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Item, id=product_id)
        cart.remove(product)
        return redirect('cart:CartDetail')
        pass

    def CartDetail(request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity':
                                                                       'update':})

        return render(request, 'cart/cart_detail.html', {'cart': cart})