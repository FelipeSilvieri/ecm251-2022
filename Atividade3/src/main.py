## Nome: Felipe Matos Silvieri
## RA: 20.00314-5
from distutils.log import info
from turtle import color
import streamlit as st
from controllers.user_controller import usercontroller as uc
from controllers.produto_controller import produtocontroller as pc

with st.sidebar:
    
    ## Inserção de credenciais ##
    nome1 = st.text_input("Nome de Usuario")
    nome2 = st.text_input("Senha",type="password")
    
    ## Checando o login ##
    uc().checkLogin(nome1,nome2)
    botao_apertado = st.checkbox("login")

if uc().checkLogin(nome1,nome2) == True and botao_apertado == True:
    
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
            
            ## Exibe Valor
            st.metric(label="Preço:",value=(pc().get_valor_numero("Notebook Acer Predator Helios-300")),delta=pc().get_valor_desconto("Notebook Acer Predator Helios-300"))
        
        ## 3o produto ##     
        
            st.image(image="assets/legion5.jpg",width=300)
            st.text(pc().get_nome("Notebook Lenovo Legion 5"))
            carrinho2 = st.checkbox(label="Adicionar ao carrinho",key=2)
            
            ## Exibe Valor    
            st.metric(label="Preço:",value=(pc().get_valor_numero("Notebook Lenovo Legion 5")),delta=pc().get_valor_desconto("Notebook Lenovo Legion 5"))
            
        with col2:
        
        ## 2o produto ##
        
            st.image(image="assets/g15.jpg",width=300)
            st.text(pc().get_nome("Notebook Dell G15"))
            carrinho3 = st.checkbox(label="Adicionar ao carrinho",key=3)
            
            ## Exibe Valor    
            st.metric(label="Preço:",value=(pc().get_valor_numero("Notebook Dell G15")),delta=pc().get_valor_desconto("Notebook Dell G15"))
        
        ## 4o produto ##   
        
            st.image(image="assets/helios500.jpg",width=300)
            st.text(pc().get_nome("Notebook Acer Predator Helios-500"))
            carrinho4 = st.checkbox(label="Adicionar ao carrinho",key=4)
            
            ## Exibe Valor    
            st.metric(label="Preço:",value=(pc().get_valor_numero("Notebook Acer Predator Helios-500")),delta=pc().get_valor_desconto("Notebook Acer Predator Helios-500"))
    
    with carrinho:
        
        ## Modelagem do Carrinho ##
        
        st.markdown("<h1 style='text-align: center; color: grey;'>Bem Vindo ao seu Carrinho!</h1>", unsafe_allow_html=True)
        
        valortotal = 0
        
        produtos_carrinho, valor_carrinho = st.columns(2)
        
        with produtos_carrinho:
            if carrinho1 == True:
                qtd1 = st.slider("Escolha a quantidade desejada",min_value=1,max_value=5,key=5)
                st.write(qtd1,(pc().get_so_nome("Notebook Acer Predator Helios-300")))
                
                valortotal += (pc().get_valor_numero("Notebook Acer Predator Helios-300"))*qtd1
                
            if carrinho2 == True:
                qtd2 = st.slider("Escolha a quantidade desejada",min_value=1,max_value=5,key=6)
                st.write(qtd2,(pc().get_so_nome("Notebook Lenovo Legion 5")))    
                
                valortotal += (pc().get_valor_numero("Notebook Lenovo Legion 5"))*qtd2
                
            if carrinho3 == True:
                qtd3 = st.slider("Escolha a quantidade desejada",min_value=1,max_value=5,key=7)
                st.write(qtd3,(pc().get_so_nome("Notebook Dell G15")))
                
                valortotal += (pc().get_valor_numero("Notebook Dell G15"))*qtd3
                
            if carrinho4 == True:
                qtd4 = st.slider("Escolha a quantidade desejada",min_value=1,max_value=5,key=8)
                st.write(qtd4,(pc().get_so_nome("Notebook Acer Predator Helios-500")))
                
                valortotal += (pc().get_valor_numero("Notebook Acer Predator Helios-500"))*qtd4
        
        with valor_carrinho:
            ## Exibição Info ##
            
            if valortotal != 0:
                st.info("Desmarque o checkbox (Página Produtos) para Remover produto do carrinho!")
            else:
                pass
            ## Exibição do valor total ##
            st.metric(label="Valor total (em R$):",value=round((valortotal),2))
            
            ## Botão de Finalizar a Compra ##
            st.button("Finalizar Compra")
    
elif uc().checkLogin(nome1,nome2) == False and botao_apertado == True:    
    ## Login inserido incorreto ##
    st.markdown("<h1 style='text-align: center; color: grey;'>ÁREA DE LOGIN</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>Digite na seção ao lado(esquerdo) as suas credenciais...</h1>", unsafe_allow_html=True)
    with st.sidebar:
        st.error("Credenciais Incorretas!")
else:    
    ## Enquanto login não efetuado ##
    st.markdown("<h1 style='text-align: center; color: grey;'>ÁREA DE LOGIN</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>Digite na seção ao lado(esquerdo) as suas credenciais...</h1>", unsafe_allow_html=True)