## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

class Product():
    def __init__(self, name, price, qtd, url):
        self._name = name
        self._price = price
        self._qtd = qtd
        self._url = url    

    def get_name(self):
        return self._name
        
    def get_price(self):
        return self._price

    def get_qtd(self):
        return self._qtd
    
    def set_qtd(self, qtd):
        self._qtd = qtd

    def get_url(self):
        return self._url
    

    def __str__(self):
        return f'Product(nome:{self.get_name()}, preço:{self.get_price()}, url:{self.get_url()}, qtd:{self.get_qtd()})'