from product import Product

class JamProduct(Product):
    def make_jam(self, quantity):
        if self.quantity >= quantity * 2:
            self.quantity -= quantity * 2
            return Product(f"Jam - {self.name}", quantity)
        else:
            print(f"Not enough {self.name} available to make jam or jam exceeds available quantity.")
            return None