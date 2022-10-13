from models.Produtos import Produto

class produtocontroller():
    
    def __init__(self) -> None:
        self.produtos = [
            (Produto("Notebook Acer Predator Helios-300",8990.99,"Um Otimo Custo-Beneficio",desconto=None)),
            (Produto("Notebook Lenovo Legion 5",7500.00,"Por um preço que cabe no se bolso","-15%")),
            (Produto("Notebook Dell G15",15000.99,"Uma supermaquina","-20%")),
            (Produto("Notebook Acer Predator Helios-500",11999.00,"Mais potente para as suas exigencias",desconto=None))
            ]
    
    def get_nome(self,nome):
        for produto in self.produtos:
            if nome == produto.titulo:
                return f'{produto.titulo}\n{produto.descricao}'
    
    def get_so_nome(self,nome):
        for produto in self.produtos:
            if nome == produto.titulo:
                return produto.titulo 
            
    def get_valor_numero(self,nome):
        for produto in self.produtos:
            if nome == produto.titulo:
                return produto.valor 
    def get_valor_desconto(self,nome):
        for produto in self.produtos:
            if nome == produto.titulo:
                return produto.desconto         
            