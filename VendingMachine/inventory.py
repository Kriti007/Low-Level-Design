class Inventory:
    def __init__(self):
        self.products = {}

    def update_quantity(self, product, qty):
        self.products[product] = qty

    def get_quantity(self, product):
        return self.products.get(product)

    def add_product(self, product, qty):
        self.products[product] = qty

    def remove_product(self, product):
        del self.products[product]

    def is_available(self, product):
        return product in self.products and self.products[product] >= 1

