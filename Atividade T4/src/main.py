## Nome: Felipe Matos Silvieri
## RA: 20.00314-5


import random
import streamlit as st

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController

p_controller = ProductController()

st.set_page_config(page_title="Silvieri Eletrônicos", page_icon="🖥️")

st.markdown("<h1 style='text-align: center; color: grey;'>Bem Vindo a Loja Silvieri Eletrônicos 🖥️</h1>", unsafe_allow_html=True)

if "Login" not in st.session_state:
    st.session_state["Profile"] = "dados"
    st.session_state["Login"] = "negado"
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
    st.session_state["falta"] = ""
    st.session_state["Cart"] = CarrinhoController()
    st.session_state["carrinho"] = ""

with st.sidebar:

    
    if st.session_state["Login"] == "negado" or st.session_state["Login"] == "errado":
        st.text("")
        st.text("")

        st.title("Página de Login 🔑")

        st.markdown("***")

        email = st.text_input(
            label="Email",
        )

        password = st.text_input(
            label="Senha",
                type = "password"
        )
        
        st.text("")
        
        col1, col2 = st.columns(2)
        with col1:
            st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),email,password))
        with col2:
            st.button(label = "Cadastrar", on_click = UserController.sign_up_screen)
    
    if st.session_state['Login'] == 'errado':

        st.markdown("***")
        st.markdown("# Email ou senha incorreto!")
        
    if st.session_state["Login"] == "registro":
        st.text("")
        st.text("")

        st.title("Página de Cadastro 🔐")

        st.markdown("***")

        name = st.text_input(
            label="Nome",
                key = 1,
        )

        email = st.text_input(
            label="Email",
                key = 2,
        )

        password = st.text_input(
            label="Senha",
                type = "password",
                    key = 3,
        )

        cpf = st.text_input(
            label="CPF",
                key = 4,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.text("")
            st.button(label= "Voltar", on_click= UserController.login_screen)
        with col2:
            st.text("")
            st.button(label= "Cadastrar", on_click= UserController.sign_up, args = (UserController(),name, email, password, cpf))

    if st.session_state["Login"] == "aprovado":

        st.text("")

        st.title(f"Bem vindo, {st.session_state['Usuario']}")
        st.markdown("***")
        st.button(label= "Sair", on_click= UserController.logout)
        st.markdown("***")

if "Login" in st.session_state:

    if st.session_state["Login"] == "aprovado":
        tab1, tab2 = st.tabs(["Home🏠", "Carrinho🛒"])

        with st.sidebar: 

            st.title("Suas Credenciais...")

            if st.session_state["Profile"] == "dados":
                st.markdown("***")
                st.markdown(f"### Nome: {st.session_state['Usuario']}")
                st.markdown("***")
                st.markdown(f"### Email: {st.session_state['Email']}")
                st.markdown("***")
                st.markdown(f"### CPF: {st.session_state['Cpf']}")
                st.markdown("***")
                st.button("Mudar informações de login", key = 7852084, on_click = UserController.change_login_data)

            if st.session_state["Profile"] == "change":
                email = st.text_input(
                    label="Novo Email",
                        key = 82700,
                )

                password = st.text_input(
                    label="Nova Senha",
                        type = "password",
                            key = 56240,
                )
                col3, col4 = st.columns(2)
                with col3:
                    st.button(label = "Voltar", key = 99785, on_click = UserController.go_back)
                
                with col4:
                    st.button(label= "Alterar", key = 1234675, on_click= UserController.change_data, args = (UserController(), email, password))
        with tab1:

            st.title("Página de Produtos")
            
            st.markdown("***")

            col1,col2 = st.columns(2,gap="large")
            
            if st.session_state["falta"]:
                st.warning(st.session_state["falta"])
            
            for i in range(0, len(p_controller.get_products()) - 1, 2):
                with col1:

                    product = p_controller.get_product(index = i)
                    st.markdown(f"## {product.get_name()}")
                    try:
                        st.image(f"{product.get_url()}")
                    except:
                        st.error("Erro ao carregar produto...")
                    st.markdown(f"## R${product.get_price()}")
                    quantity1 = st.number_input(label = "", key = 100 * (i+1), format = "%i", step = 1,min_value = 1, max_value = product.get_qtd())
                    if product.get_qtd() > 0 and product.get_qtd() - quantity1 >= 0:
                        st.button(label = f"Adicionar {product.get_name()}", key = 200 * (i+12), on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
                    else:
                        st.markdown(f"## {product.get_name()} Sem Estoque!")
                with col2:

                    product = p_controller.get_product(index = i + 1)
                    st.markdown(f"## {product.get_name()}")
                    try:
                        st.image(f"{product.get_url()}")
                    except:
                        st.error("Erro ao carregar produto...")
                    st.markdown(f"## R${product.get_price()}")
                    quantity2 = st.number_input(label = "",  format = "%i", key = 300 * (i+83), step = 1,min_value = 1, max_value = product.get_qtd())
                    if product.get_qtd() > 0 and product.get_qtd() - quantity2 >= 0:    
                        st.button(label = f"Adicionar {product.get_name()}", key = 400 * (i+99), on_click= st.session_state["Cart"].add_product, args = (product, quantity2))
                    else:
                        st.markdown(f"## {product.get_name()} Sem Estoque!")

        with tab2:

            st.title("Bem Vindo ao seu Carrinho!")
            st.markdown("Obs: estão listados abaixos os produtos no seu carrinho")

            st.markdown("***")

            col1, col2, col3 = st.columns(3,gap="large")
            col1.markdown("### Produto")
            col2.markdown("### Preço")
            col3.markdown("### Quantidade")
            
            product_qtd = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtd.append(produquantity[1])
                    
            with col1:

                for i in range(len(product_names)):
                    st.markdown(f"### {product_names[i]}")


            with col2:

                for i in range(len(product_names)):
                    st.markdown(f"## R${product_prices[i]}")


            with col3:

                
                for i in range(len(product_names)):
                    st.markdown(f"## x{product_qtd[i]}")   

            st.markdown("***")
            valor_total = st.session_state["Cart"].get_total_price()
            
            st.markdown(f"## Valor total: R${valor_total:.2f} ")
            st.button(label = "Finalizar Pedido", key = 998, on_click= st.session_state["Cart"].clear_cart)
            st.text("Obs: Equivalente a Limpar Carrinho")
        
