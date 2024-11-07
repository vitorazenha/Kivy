from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class PriceComparatorApp(App):
    def build(self):
        self.products = []  # Lista para armazenar os produtos e preços
        return BoxLayout()

    def add_product(self):
        # Obter o nome e o preço do produto
        product_name = self.root.ids.product_name.text
        product_price = self.root.ids.product_price.text

        if product_name and product_price:
            try:
                # Converter o preço para float
                price = float(product_price)
                # Adicionar o produto à lista
                self.products.append((product_name, price))
                self.root.ids.result_label.text = f"Produto '{product_name}' adicionado!"
            except ValueError:
                self.root.ids.result_label.text = "Erro: preço inválido."
        else:
            self.root.ids.result_label.text = "Por favor, preencha ambos os campos."

        # Limpar campos
        self.root.ids.product_name.text = ""
        self.root.ids.product_price.text = ""

    def compare_prices(self):
        if not self.products:
            self.root.ids.result_label.text = "Nenhum produto na lista para comparar."
            return

        # Encontrar o produto com o menor preço
        cheapest_product = min(self.products, key=lambda x: x[1])
        self.root.ids.result_label.text = f"O produto mais barato é '{cheapest_product[0]}' custando R${cheapest_product[1]:.2f}"

    def clear_list(self):
        self.products = []
        self.root.ids.result_label.text = "Lista de produtos limpa!"

if __name__ == '__main__':
    PriceComparatorApp().run()
