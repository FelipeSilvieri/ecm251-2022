from models.Produtos import Produto

class produtocontroller():
    
    def __init__(self) -> None:
        self.produtos = [
            (Produto("Notebook Acer Predator Helios-300",8990.99,"Um Otimo Custo-Beneficio")),
            (Produto("Notebook Lenovo Legion 5",7500.00,"Por um preço que cabe no se bolso")),
            (Produto("Notebook Dell G15",15000.99,"Uma supermaquina")),
            (Produto("Notebook Acer Predator Helios-500",11999.00,"Mais potente para as suas exigencias"))
            ]
    def get_nome(self,nome):
        for produto in self.produtos:
            if nome == produto.titulo:
                return f'{produto.titulo}\nValor:{produto.valor}\n{produto.descricao}'