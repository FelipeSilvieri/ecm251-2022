## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

class Produto:
    def __init__(self,titulo,valor,descricao) -> None:
        self.titulo = titulo
        self.valor = valor
        self.descricao = descricao
    def __str__(self) -> str:
        return f'{self.titulo}\nValor:{self.valor}\n{self.descricao}' 
