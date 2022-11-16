## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

import streamlit as st
import time
from models.product import Product
from dao.product_dao import ProductDAO

class ProdutoController:
    
    def __init__(self):
        self._products = ProductDAO.get_instance().get_all()

    def get_product(self,index):
        return self._products[index]
    
    def get_products(self):
        return self._products


    