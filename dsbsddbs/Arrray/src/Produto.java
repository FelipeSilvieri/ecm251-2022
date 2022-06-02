public abstract class Produto {

    public final double preço;
    public final double tamanho;
   
    public Produto(double preço, double tamanho) {
        this.preço = preço;
        this.tamanho = tamanho;
    }

    public double getPreço() {
        return preço;
    }

    public double getTamanho() {
        return tamanho;
    }
    
    
}
