class Produkts:
    def __init__(self, name, quantity=0):
        self.name = name
        self.quantity = quantity

    def add_quantity(self, quantity):
        self.quantity += quantity

    def consume(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print(f"Nepietiek {self.name} priekš izmantošanas.")

    def __str__(self):
        return f"{self.name} ({self.quantity} kg)"