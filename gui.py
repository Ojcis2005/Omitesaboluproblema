import PySimpleGUI as sg

class Product:
    def __init__(self, name, quantity=0):
        self.name = name
        self.quantity = quantity

    def add_quantity(self, quantity):
        self.quantity += quantity

    def consume(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print(f"Not enough {self.name} available for consumption.")

    def make_jam(self, products):
        if self.quantity >= 2:  # Require 2 kg of the product to make 1 kg of jam
            self.quantity -= 2
            jam_name = f"Jam from {self.name}"
            jam_product = Product(jam_name, 1.0)
            products.append(jam_product)
        else:
            print(f"Not enough {self.name} available to make jam.")

    def __str__(self):
        return f"{self.name} ({self.quantity} kg)"

def create_layout(products):
    product_list = [str(product) for product in products]
    layout = [
        [sg.Text('Product Name:'), sg.InputText(key='product_name')],
        [sg.Text('Product Quantity (kg):'), sg.InputText(key='product_quantity')],
        [sg.Button('Add Product'), sg.Button('Consume Product'), sg.Button('Edit Product')],
        [sg.Text('Product List:')],
        [sg.Listbox(values=product_list, size=(40, 6), key='product_list')],
        [sg.TabGroup([[
            sg.Tab('Make Jam', create_jam_layout(products), key='-TABJAM-')
        ]])]
    ]
    return layout

def create_jam_layout(products):
    product_names = [product.name for product in products]
    layout = [
        [sg.Text('Select a product to make jam from:')],
        [sg.Combo(product_names, key='selected_product')],
        [sg.Button('Make Jam')],
    ]
    return layout

def main():
    products = []
    window = sg.Window('Product Tracker', create_layout(products))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Add Product':
            name = values['product_name']
            quantity = float(values['product_quantity']) if values['product_quantity'] else 0.0
            products.append(Product(name, quantity))
            product_list = [str(product) for product in products]
            window['product_list'].update(values=product_list)

        if event == 'Consume Product':
            selected_product = window['product_list'].get()
            if selected_product:
                product_info = selected_product[0]
                name = product_info.split(' (')[0]  # Extract product name
                quantity = float(values['product_quantity']) if values['product_quantity'] else 0.0
                for product in products:
                    if product.name == name:
                        product.consume(quantity)
                product_list = [str(product) for product in products]
                window['product_list'].update(values=product_list)

        if event == 'Edit Product':
            selected_product = window['product_list'].get()
            if selected_product:
                product_info = selected_product[0]
                name = product_info.split(' (')[0]  # Extract product name
                new_name = values['product_name']
                if new_name:
                    for product in products:
                        if product.name == name:
                            product.name = new_name
                    product_list = [str(product) for product in products]
                    window['product_list'].update(values=product_list)

        if event == 'Make Jam':
            selected_product_name = values['selected_product']
            for product in products:
                if product.name == selected_product_name:
                    product.make_jam(products)
            product_list = [str(product) for product in products]
            window['product_list'].update(values=product_list)

    window.close()

if __name__ == "__main__":
    main()
