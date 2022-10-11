## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

class User:
    def __init__(self,nome,email,senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha
    def __str__(self) -> str:
        return f'Usuario:{self.nome},Email:{self.email},Senha:{self.senha}'