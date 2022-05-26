public class App {
    public static void main(String[] args) throws Exception {
        Produto cornDog = new Comida(12.5, "Corn dog", 5, "Cachorro quente diferenciado", EnumCategoriaComida.COREANA, EnumAlergicos.GLUTEN, EnumPimenta.SUAVE);

        Produto acaiMoleza = new Bebida(10, "Açai do Molezolas", 7, "Açai top maravilhoso", EnumCategoriaBebida.SUCO, EnumTemperatura.FRIO);

        System.out.println("Preços Regulares: ");
        System.out.println(cornDog.getNome()+ ":R$" + cornDog.getPreco());
        System.out.println(acaiMoleza.getNome()+":R$" +acaiMoleza.getPreco());

        System.out.println("Preços c/ Desconto: ");
        System.out.println(cornDog.getNome()+ ":R$" + precoComDesconto(cornDog));
        System.out.println(acaiMoleza.getNome()+":R$" +precoComDesconto(acaiMoleza));

        
    }
    public static String precoComDesconto(IGerarDesconto produto) {
        return "R$:" + produto.gerarDesconto();
        
    }
}    
