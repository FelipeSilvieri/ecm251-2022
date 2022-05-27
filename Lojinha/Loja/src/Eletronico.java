public class Eletronico extends Produtos{
    
    public final EnumTipoBrinquedo tipobrinquedo;
    public final EnumTipoEletronico tipoeletronico;
    
    public Eletronico(EnumTipoBrinquedo tipobrinquedo, EnumTipoEletronico tipoeletronico) {
        
        super(cor,preco, descricao, tipo, precofinal);
        this.tipobrinquedo = tipobrinquedo;
        this.tipoeletronico = tipoeletronico;
    }

    
    



    
}
