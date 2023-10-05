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

    def __str__(self):
        return f"{self.name} ({self.quantity} kg)"

def create_layout(products):
    product_list = [str(product) for product in products]
    sg.theme('DarkGreen4')  # Set the background color to green
    layout = [
        [sg.Text('Product Name:'), sg.InputText(key='product_name')],
        [sg.Text('Product Quantity (kg):'), sg.InputText(key='product_quantity')],
        [sg.Button('Add Product', button_color=('white', 'red')), sg.Button('Consume Product', button_color=('white', 'red')),
         sg.Button('Make Jam', button_color=('white', 'red')), sg.Button('Edit Product', button_color=('white', 'red'))],
        [sg.Text('Product List:')],
        [sg.Listbox(values=product_list, size=(40, 6), key='product_list')],
        [sg.Button('Exit', button_color=('white', 'red'))],  # Change the exit button color to red
    ]
    return layout

def main():
    products = []
    window = sg.Window('Product Tracker', create_layout(products))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
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

        if event == 'Make Jam':
            selected_product = window['product_list'].get()
            if selected_product:
                product_info = selected_product[0]
                name = product_info.split(' (')[0]  # Extract product name
                quantity = float(values['product_quantity']) if values['product_quantity'] else 0.0
                for product in products:
                    if product.name == name:
                        jam_product = product.make_jam(quantity)
                        if jam_product:
                            products.append(jam_product)
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

    window.close()

if __name__ == "__main__":
    main()