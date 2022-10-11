from models.Produtos import Produto
from pages.Home import Home

class carrinhocontroller():
    
    def valortotal():
        return float(Home.produto1.valor())
        pass