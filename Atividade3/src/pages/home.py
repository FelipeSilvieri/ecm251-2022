## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

from importlib.machinery import FileFinder
from tkinter.tix import COLUMN
from turtle import home
from PIL import Image
import streamlit as st
from models.Produtos import Produto
from controllers.carrinho_controller import carrinhocontroller as cc
from pages.Carrinho import Carrinho

class Home:
    
    ## Título HomePage ##
    
    st.markdown("<h1 style='text-align: center; color: grey;'>BEM VINDO(A) À LOJA DIGITAL SILVIERI ELETRÔNICOS</h1>", unsafe_allow_html=True)
        
    ## Criando Objetos de produto ##
    
    produto1 = Produto("Notebook Acer Predator Helios-300",8990.99,"Um Otimo Custo-Beneficio")
    produto2 = Produto("Notebook Dell Inspire Gaming",7500.00,"Por um preço que cabe no se bolso")
    produto3 = Produto("Notebook Alienware Gamer",15000.99,"Uma supermaquina")
    produto4 = Produto("Notebook Acer Predator Helios-500",11999.00,"Mais potente para as suas exigencias")
       
    ## Exibição dos Produtos ##
    
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/helios300.jpg")
    with col2:
        st.image("assets/helios300.jpg")
    with col1:
        st.text(produto1)
    with col2:
        st.text(produto2)
        
    with col1:
        if st.button("Carrinho","adicionar1"):
            qtd1 = Carrinho.Carrinho1.pr1 + 1
            
    with col2:
        if st.button("Carrinho","adicionar2"):
            qtd2 = Carrinho.Carrinho1.pr2 + 1
            
    with col1:
        st.text(Carrinho.Carrinho1.pr1)
    with col2:
        st.text(Carrinho.Carrinho1.pr2)
    
    qtd1 = int
        
    with col1:
        if st.button("Carrinho","adicionar1"):
            qtd1 = Carrinho.Carrinho1.pr1 + 1

    with col2:
        if st.button("Carrinho","adicionar2"):
            Carrinho.Carrinho1.pr2 += 1
    
    with col1:
        st.text(Carrinho.Carrinho1.pr3) 
    
    with col2:
        st.text(Carrinho.Carrinho1.pr4) 
        
    ## Mostrando quantidades ##
    
    with col1:
        st.text(Carrinho.Carrinho1.pr1) 

    with col2:
        st.text(Carrinho.Carrinho1.pr2) 
    
    with col1:
        if st.button("Carrinho","adicionar3"):
            Carrinho.Carrinho1.pr3 += 1
   
    with col2:
        if st.button("Carrinho","adicionar4"):
            Carrinho.Carrinho1.pr4 += 1
    
    pass      
        
    
            
            
