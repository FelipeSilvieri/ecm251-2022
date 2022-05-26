public class Bebida extends Produto{

    public final EnumCategoriaBebida categoria;
    public final EnumTemperatura temperatura;
   
    public Bebida(double preco, String nome, int quantidade, String descricao, EnumCategoriaBebida categoria,
            EnumTemperatura temperatura) {
        super(preco, nome, quantidade, descricao);
        this.categoria = categoria;
        this.temperatura = temperatura;
    }

    @Override
    public double gerarDesconto() {
        // 10% de desconto        
        return getPreco()*0.9;
    }

}
