## Nome: Felipe Matos Silvieri
## RA: 20.00314-5
from distutils.log import info
import streamlit as st
from controllers.user_controller import usercontroller
from controllers.produto_controller import produtocontroller as pc

with st.sidebar:
    
    nome1 = st.text_input("Nome de Usuario")
    nome2 = st.text_input("Senha",type="password")
    
    usercontroller().checkLogin(nome1,nome2)
    botao_apertado = st.checkbox("login")

if usercontroller().checkLogin(nome1,nome2) == True and botao_apertado == True:
    with st.sidebar:
        st.success("Login Efetuado com Sucesso!")
    produtos, carrinho = st.tabs(["Produtos","Carrinho"])
    with produtos:
        
    ## Título HomePage ##
    
        st.markdown("<h1 style='text-align: center; color: grey;'>Bem Vindo a Loja Silvieri Eletrônicos</h1>", unsafe_allow_html=True)
        
        ## Exibição dos Produtos ##
        
        col1, col2 = st.columns(2)

        with col1:
         
        ## 1o produto ##    
            st.image(image="assets/helios300.jpg",width=300)
            st.text(pc().get_nome("Notebook Acer Predator Helios-300"))
            carrinho1 = st.checkbox(label="Adicionar ao carrinho",key=1)
        
        ## 3o produto ##     
        
            st.image(image="assets/legion5.jpg",width=300)
            st.text(pc().get_nome("Notebook Lenovo Legion 5"))
            carrinho2 = st.checkbox(label="Adicionar ao carrinho",key=2)
        
        with col2:
        
        ## 2o produto ##
        
            st.image(image="assets/g15.jpg",width=300)
            st.text(pc().get_nome("Notebook Dell G15"))
            carrinho3 = st.checkbox(label="Adicionar ao carrinho",key=3)
        
        ## 4o produto ##   
        
            st.image(image="assets/helios500.jpg",width=300)
            st.text(pc().get_nome("Notebook Acer Predator Helios-500"))
            carrinho4 = st.checkbox(label="Adicionar ao carrinho",key=4)
    
    with carrinho:
    
        st.markdown("<h1 style='text-align: center; color: grey;'>Bem Vindo ao seu Carrinho!</h1>", unsafe_allow_html=True)
        
        valortotal = 0
        
        if carrinho1 == True:
            st.write(1,(pc().get_so_nome("Notebook Acer Predator Helios-300")))
            st.write(pc().get_so_valor("Notebook Acer Predator Helios-300"))
            valortotal += pc().get_valor_numero("Notebook Acer Predator Helios-300")
        if carrinho2 == True:
            st.write(1,(pc().get_so_nome("Notebook Lenovo Legion 5")))    
            st.write(pc().get_so_valor("Notebook Lenovo Legion 5"))
            valortotal += pc().get_valor_numeror("Notebook Lenovo Legion 5")
        if carrinho3 == True:
            st.write(1,(pc().get_so_nome("Notebook Dell G15")))
            st.write(pc().get_so_valor("Notebook Dell G15"))
            valortotal += pc().get_valor_numero("Notebook Dell G15")
        if carrinho4 == True:
            st.write(1,(pc().get_so_nome("Notebook Acer Predator Helios-500")))
            st.write(pc().get_so_valor("Notebook Acer Predator Helios-500")) 
            valortotal += pc().get_valor_numero("Notebook Acer Predator Helios-500")
        
        st.metric("Valor total:",round((valortotal),2))
        st.button("Finalizar Compra")
    
else:    
    st.markdown("<h1 style='text-align: center; color: grey;'>ÁREA DE LOGIN</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>Digite na seção ao lado(esquerdo) as suas credenciais...</h1>", unsafe_allow_html=True)
    
    
    



