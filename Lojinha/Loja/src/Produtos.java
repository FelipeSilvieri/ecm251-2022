public abstract class Produtos implements IPrecoFinal{

    private final String cor;
    private final double preco;
    private final String descricao;
    private final String tipo;
    private final double precofinal;


    public Produtos(String cor, double preco, String descricao, String tipo, double precofinal) {
        this.cor = cor;
        this.preco = preco;
        this.descricao = descricao;
        this.tipo = tipo;
        this.precofinal = precofinal;
    }

    public String getTipo() {
        return tipo;
    }

    public String getCor() {
        return cor;
    }

    public double getPreco() {
        return preco;
    }

    public String getDescricao() {
        return descricao;
    }

    public double getPrecofinal() {
        return precofinal;
    }
    
    
}
