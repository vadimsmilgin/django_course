from django.conf import settings
from shop.models import Item


class Cart:
    def __init__(self, request):

        # инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину пользователя или обновение
    def add(self, product, quantity = 1, update_quantity = False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                    }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Итерация по товарам
    def __iter__(self):
        products = Item.objects.filter(id__in=self.cart.keys())
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = item['price']
            item['total_price'] = float(item['price']) * float(item['quantity'])
            yield item

    def items_count(self):
        return sum(item['quantity'] for item in self.cart.values())
        pass

    def get_total_price(self):
        return sum(float(item['price']) * float(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        pass

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
