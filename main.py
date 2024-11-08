from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout as KivyBoxLayout

class ComparadorApp(MDApp):
    def build(self):
        self.products = []  # Lista para armazenar os produtos e preços

        # Layout principal da interface
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Campo para o nome do produto
        self.product_name_field = MDTextField(hint_text="Nome do Produto", size_hint=(1, 0.1))
        self.layout.add_widget(self.product_name_field)

        # Campo para o preço do produto
        self.product_price_field = MDTextField(hint_text="Preço do Produto", input_filter="float", size_hint=(1, 0.1))
        self.layout.add_widget(self.product_price_field)

        # Botão para adicionar produto
        self.add_button = MDRaisedButton(text="Adicionar Produto", size_hint=(1, 0.1))
        self.add_button.bind(on_press=self.add_product)
        self.layout.add_widget(self.add_button)

        # Botão para comparar preços
        self.compare_button = MDRaisedButton(text="Comparar Preços", size_hint=(1, 0.1))
        self.compare_button.bind(on_press=self.compare_prices)
        self.layout.add_widget(self.compare_button)

        # Botão para limpar lista
        self.clear_button = MDRaisedButton(text="Limpar Lista", size_hint=(1, 0.1))
        self.clear_button.bind(on_press=self.clear_list)
        self.layout.add_widget(self.clear_button)

        # Label para exibir o resultado
        self.result_label = MDLabel(text="Resultado aparecerá aqui", size_hint=(1, 0.2), halign="center")
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
