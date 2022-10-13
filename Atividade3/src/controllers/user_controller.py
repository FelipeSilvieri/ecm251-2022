## Nome: Felipe Matos Silvieri
## RA: 20.00314-5
import string
import streamlit as st
from models.user import User

class usercontroller():
    
    def __init__(self) -> None:
        self.users = [
            (User("Felipe Silvieri","felipesilvieri@bol.com","felipe123")),
            (User("Murilove","murilovedoslove@bol.com","murilo321")),
            (User("Ademilson Freitas","adreitas@gmail.com","ademilsolas123"))
            ]

    def checkUser(self,usuario):
        return usuario in self.users
    
    def checkLogin(self,nometeste,senhateste):
        user_teste = User(nome=nometeste,email=None,senha=senhateste)
        for usuario in self.users:
            if usuario.nome  == user_teste.nome and usuario.senha == user_teste.senha:
                return True
        return False
     