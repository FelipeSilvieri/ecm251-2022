public class Leitura extends Produto{

    public final EnumGenero genero;
    private String editora;
    private int paginas;
    
 
    public Leitura(double preco, String nome, int quantidade, String descricao, EnumGenero genero, String editora, int paginas) {
        super(preco, nome, quantidade, descricao);
        this.genero = genero;
        this.editora = editora;
        this.setPaginas(paginas);
    }

    public int getPaginas() {
        return paginas;
    }

    public void setPaginas(int paginas) {
        this.paginas = paginas;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }

    @Override
    public double gerarDesconto() {
        // 30% de desconto
        return getPreco()*0.7;
    }   
    
   
}
