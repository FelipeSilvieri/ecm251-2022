public class Comida extends Produto{
    public final EnumCategoriaComida categoria;
    public final EnumAlergicos alergicos;
    public final EnumPimenta pimenta;
    
    public Comida(double preco, String nome, int quantidade, String descricao, EnumCategoriaComida categoria,
            EnumAlergicos alergicos, EnumPimenta pimenta) {
        super(preco, nome, quantidade, descricao);
        this.categoria = categoria;
        this.alergicos = alergicos;
        this.pimenta = pimenta;
    }

    @Override
    public double gerarDesconto() {
        // 5% de desconto        
        return getPreco()*0.95;
    }

}
