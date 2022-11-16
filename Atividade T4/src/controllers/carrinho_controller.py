## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

import streamlit as st
from models.carrinho import Carrinho
from src.dao.product_dao import ProductDAO

class CarrinhoController():
    def __init__(self):
        self._cart = Carrinho()
        
    def get_cart(self):
        return self._cart

    def add_product(self,product,quantity):
        for i in range(len(self.get_cart().get_products())):
            if self.get_cart().get_products()[i][0].get_name() == product.get_name() and quantity <= product.get_qtd():
                if self.get_cart().get_products()[i][1] + quantity <= product.get_qtd():
                    self.get_cart().get_products()[i][1] += quantity
                    st.session_state["falta"] = ""
                    
                else:
                    st.session_state["falta"] = f"{product.get_name()} tem somente {product.get_qtd()} unidades disponíveis no estoque"
                return
        self.get_cart().get_products().append([product,quantity])

    def get_total_price(self):
        total = 0
        for items in self.get_cart().get_products():
            total += items[0].get_price() * items[1]
        return total
    
    def clear_cart(self):
        try:
            for item in self.get_cart().get_products():
                if item[0].get_qtd() - item[1] >= 0:
                    item[0].set_qtd(item[0].get_qtd() - item[1])
                ProductDAO.get_instance().update_product(item[0])
            self.get_cart().set_products([])
            return True
        except:
            return False
        
    def remove_cart(self):
        try:
            for item in self.get_cart().get_products():
                item[0].set_qtd(item[0].get_qtd() - 1)
                ProductDAO.get_instance().update_product(item[0])
            self.get_cart().set_products([])
            return True
        except:
            return False
