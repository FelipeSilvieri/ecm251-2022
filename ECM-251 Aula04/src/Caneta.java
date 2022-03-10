public class Caneta {
    String modelo;
    String cor;
    int carga;
    double ponta;
    final int CARGA_INICIAL = 100;

    void iniciarCaneta(String cor, String modelo, int carga, double ponta) {
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
        this.carga = CARGA_INICIAL; // Representa os 100% da carga inicial na compra da caneta

    }

    void escrever(String texto) {
        for(int i = 0; i < texto.length(); i++){
            if(this.carga > 0){
                System.out.print(texto.charAt(i));
                this.carga -= 1;
            }
                else{
                    System.out.print("\nCaneta sem carga");
                    break;
            }            
        }

    }

    String mostrarDados() {
        return "Modelo: " + this.modelo +
                " - Cor: " + this.cor +
                " - Ponta: " + this.ponta +
                " - Carga: " + this.carga;
    }

}
