public class Caneta extends Produto implements ICalcula{
    
    private final EnumCorCaneta corCaneta;
    private final EnumMarcaCaneta marcaCaneta;
    private final double ponta;
    private final int carga;
    
    public Caneta(double preço, double tamanho, EnumCorCaneta corCaneta, EnumMarcaCaneta marcaCaneta, double ponta,
            int carga) {
        super(preço, tamanho);
        this.corCaneta = corCaneta;
        this.marcaCaneta = marcaCaneta;
        this.ponta = ponta;
        this.carga = carga;
    }
    public EnumCorCaneta getCorCaneta() {
        return corCaneta;
    }
    public EnumMarcaCaneta getMarcaCaneta() {
        return marcaCaneta;
    }
    public double getPonta() {
        return ponta;
    }
    public int getCarga() {
        return carga;
    }
    
    @Override
    public double calculo() {
        return getPreço()/getTamanho();
    }

}
