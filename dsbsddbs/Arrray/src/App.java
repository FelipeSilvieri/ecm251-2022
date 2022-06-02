public class App {
    public static void main(String[] args) throws Exception {

    Caneta canetola = new Caneta(75, 15, EnumCorCaneta.AZUL, EnumMarcaCaneta.FABERCASTELL, 3, 89);

    System.out.println("A caneta custa R$: " + canetola.getPreço() + " em um total de: " + canetola.calculo() + " Reais/cm");

    if(canetola.calculo() <= 5 ){
        System.out.println("A caneta possui um bom custo beneficio");
    }else{
        System.out.println("A caneta ñ possui um bom custo benefício");
    }

    }
}
