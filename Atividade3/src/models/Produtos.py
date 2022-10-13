## Nome: Felipe Matos Silvieri
## RA: 20.00314-5

class Produto:
    def __init__(self,titulo,valor,descricao,desconto) -> None:
        self.titulo = titulo
        self.valor = valor
        self.descricao = descricao
        self.desconto = desconto
    def __str__(self) -> str:
        return f'{self.titulo}\n{self.descricao}' 
