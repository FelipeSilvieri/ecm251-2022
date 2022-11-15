## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

class Carrinho():

    def __init__(self):
        self._products=[]

    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products
        
    def __str__(self):
        return self._products