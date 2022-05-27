public class Eletronico extends Produtos{
    
    public final EnumTipoBrinquedo tipobrinquedo;
    public final EnumTipoEletronico tipoeletronico;
    
    public Eletronico(String cor, double preco, String descricao, String tipo, double precofinal, EnumTipoBrinquedo tipobrinquedo, EnumTipoEletronico tipoeletronico) {
        super(cor,preco, descricao, tipo, precofinal);
        this.tipobrinquedo = tipobrinquedo;
        this.tipoeletronico = tipoeletronico;
    }

    
    



    
}
