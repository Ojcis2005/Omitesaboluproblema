import PySimpleGUI as sg

def create_layout(products):
    layout = [
        [sg.Text('Lauku labuma nosaukums:'), sg.InputText(key='product_name')],
        [sg.Text('Daudzums'), sg.InputText(key='product_quantity')],
        [sg.Button('Pievienot labumu'), sg.Button('Izmantot labumu'), sg.Button('Izveidot ievārjijumu'), sg.Button('Rediģēt labumu')],
        [sg.Text('Labumu Saraksts:')],
        [sg.Listbox(values=[str(product) for product in products], size=(40, 6), key='product_list')],
        [sg.Button('Iziet')],
    ]
    return layout

def main():
    products = []
    window = sg.Window('Produkta Izsekotājs', create_layout(products))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Iziet':
            break

        if event == 'Pievienot labumu':
            name = values['product_name']
            quantity = float(values['product_quantity']) if values['product_quantity'] else 0.0
            products.append(products(name, quantity))
            window['product_list'].update(products)

        if event == 'Consume Product':
            selected_product = window['product_list'].get()
            if selected_product:
                product = selected_product[0]
                name = product.name
                quantity = float(values['product_quantity']) if values['product_quantity'] else 0.0
                for p in products:
                    if p.name == name:
                        p.consume(quantity)
                window['product_list'].update(products)

        if event == 'Izveidot ievārjijumu':
            selected_product = window['product_list'].get()
            if selected_product:
                product = selected_product[0]
                name = product.name
                quantity = float(values['product_quantity']) if values['product_quantity'] else 0.0
                for p in products:
                    if p.name == name:
                        jam_product = p.make_jam(quantity)
                        if jam_product:
                            products.append(jam_product)
                window['product_list'].update(products)

        if event == 'Rediģēt labumu':
            selected_product = window['product_list'].get()
            if selected_product:
                product = selected_product[0]
                name = product.name
                new_name = values['product_name']
                if new_name:
                    product.name = new_name
                window['product_list'].update(products)

    window.close()

if __name__ == "__main__":
    main()