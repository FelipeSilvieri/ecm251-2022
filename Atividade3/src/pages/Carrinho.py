## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

import streamlit as st
from pages.home import Home
from controllers.carrinho_controller import carrinhocontroller as cc

class Carrinho:
    
    Carrinho1 = cc(1,4,3,6)
    
    st.title("Seu Carrinho de Compras 🛒:")
    
    st.markdown("<h4 style='text-align: center; color: white;'>Total de Itens</h4>", unsafe_allow_html=True)
    
    if Carrinho1.pr1 != 0:
        st.write(Carrinho1.pr1,"x",Home.produto1.titulo)
    else:
        pass
    if Carrinho1.pr2 != 0:
        st.write(Carrinho1.pr2,"x",Home.produto2.titulo)
    else:
        pass
    if Carrinho1.pr3 != 0:
        st.write(Carrinho1.pr3,"x",Home.produto3.titulo)
    else:
        pass
    if Carrinho1.pr4 != 0:
        st.write(Carrinho1.pr4,"x",Home.produto4.titulo)
    else:
        pass
    
    valorCarrinho = (Home.produto1.valor*Carrinho1.pr1)+(Home.produto2.valor*Carrinho1.pr2)+(Home.produto3.valor*Carrinho1.pr3)+(Home.produto4.valor*Carrinho1.pr4)
    
    st.markdown("<h4 style='text-align: center; color: white;'></h4>", unsafe_allow_html=True)
    st.metric(label="Total (em R$): ", value = valorCarrinho)
    st.button("Finalizar Compra") 
    
    