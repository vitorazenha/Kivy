from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ComparadorApp(App):
    def build(self):
        self.products = []  # Lista para armazenar os produtos e preços

        # Layout principal da interface
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Campo para o nome do produto
        self.product_name_field = TextInput(hint_text="Nome do Produto", size_hint=(1, 0.1))
        self.layout.add_widget(self.product_name_field)

        # Campo para o preço do produto
        self.product_price_field = TextInput(hint_text="Preço do Produto", input_filter="float", size_hint=(1, 0.1))
        self.layout.add_widget(self.product_price_field)

        # Botão para adicionar produto
        self.add_button = Button(text="Adicionar Produto", size_hint=(1, 0.1))
        self.add_button.bind(on_press=self.add_product)
        self.layout.add_widget(self.add_button)

        # Botão para comparar preços
        self.compare_button = Button(text="Comparar Preços", size_hint=(1, 0.1))
        self.compare_button.bind(on_press=self.compare_prices)
        self.layout.add_widget(self.compare_button)

        # Botão para limpar lista
        self.clear_button = Button(text="Limpar Lista", size_hint=(1, 0.1))
        self.clear_button.bind(on_press=self.clear_list)
        self.layout.add_widget(self.clear_button)

        # Label para exibir o resultado
        self.result_label = Label(text="Resultado aparecerá aqui", size_hint=(1, 0.2))
        self.layout.add_widget(self.result_label)

        return self.layout

    def add_product(self, instance):
        # Obter o nome e preço do produto
        product_name = self.product_name_field.text
        product_price = self.product_price_field.text

        if product_name and product_price:
            try:
                # Converter o preço para float e adicionar o produto à lista
                price = float(product_price)
                self.products.append((product_name, price))
                self.result_label.text = f"Produto '{product_name}' adicionado com sucesso!"
            except ValueError:
                self.result_label.text = "Erro: Insira um preço válido."
        else:
            self.result_label.text = "Por favor, preencha ambos os campos."

        # Limpar os campos de entrada
        self.product_name_field.text = ""
        self.product_price_field.text = ""

    def compare_prices(self, instance):
        if not self.products:
            self.result_label.text = "Nenhum produto na lista para comparar."
            return

        # Encontrar o produto com o menor preço
        cheapest_product = min(self.products, key=lambda x: x[1])
        self.result_label.text = f"O produto mais barato é '{cheapest_product[0]}' custando R${cheapest_product[1]:.2f}"

    def clear_list(self, instance):
        # Limpar a lista de produtos e o resultado
        self.products = []
        self.result_label.text = "Lista de produtos limpa!"

if __name__ == "__main__":
    ComparadorApp().run()
