## Nome: Felipe Matos Silvieri
## RA: 20.00314-5
from distutils.log import info
import streamlit as st
from models.Produtos import Produto



if (st.text_input("Pessoa") != "123"):
    home = st.tabs(["Home"])
else:    
    produtos, carrinho = st.tabs(["Produtos","Carrinho"])
    with produtos:
        
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



with st.sidebar:
   
    st.markdown("<h1 style='text-align: center; color: grey;'>ÁREA DE LOGIN</h1>", unsafe_allow_html=True)
        
    st.text_input("Usuario")
    st.text_input("Senha")
    st.button("login")