## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

import streamlit as st
from src.models.user import User
from controllers.carrinho_controller import CarrinhoController
from src.dao.user_dao import UserDAO

class UserController():
    def __init__(self):
        
        ## Carrega as credenciais de todos os usuários ##
        self._users = UserDAO.get_instance().get_all()

    def check_login(self, email, password):
        user_dict = {}
        for user in self._users:
            user_email = user.get_email()
            passw = user.get_password()
            user_dict[user_email] = (passw, [user.get_name(), user.get_cpf()])

        try:
            if user_dict[email][0] == password:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = user_dict[email][1][0] # Nome
                st.session_state['Cpf'] = user_dict[email][1][1]     # CPF
                st.session_state['Email'] = email                    # Email
                
            else:
                st.session_state["Login"] = "errado"

        except KeyError:

            st.session_state["Login"] = "errado"
            

    def sign_up(self, name, email, password, cpf):
        user = User(name, email, password, cpf)
       
        try:
            UserDAO.get_instance().insert_user(user)
            st.markdown("### Registrado")
        except:
            st.markdown("### Email ou cpf já registrados")

    def logout():
        st.session_state["Login"] = "negado"
        st.session_state["Cart"] = CarrinhoController()
    
    def change_data(self, email, password):
        user = User(st.session_state['Usuario'], email, password, st.session_state['Cpf'])
        try:
            UserDAO.get_instance().update_user(user)
            st.markdown("### Alterações efetuadas com sucesso")
        except:
            st.markdown("### Esse Email já foi préviamente registrado")
    
    def change_login_data():
        st.session_state["Profile"] = "change"

    def go_back():
        st.session_state["Profile"] = "dados"
    
    def sign_up_screen():
        st.session_state["Login"] = "registro"
    
    def login_screen():
        st.session_state["Login"] = "negado"
    
    def home_screen():
        st.session_state["Login"] = "negado"
        st.session_state["Login"] = "aprovado"