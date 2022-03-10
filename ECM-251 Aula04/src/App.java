public class App {
    public static void main(String[] args) throws Exception {
        //Cria e instancia um objeto do tipo caneta
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("Azul", "BIC", 100, 1.0);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Verde", "Kibe", 100, 0.5);
  
        c1.escrever("Ola Mundo o Batman Novo é um bom Filme ");
        c2.escrever("Bom dia");
        
        c1.escrever("\nOla Mundo o Batman Novo é um bom Filme ");
        c2.escrever("Bom dia");

        c1.escrever("\nOla Mundo o Batman Novo é um bom Filme ");
        c2.escrever("Bom dia");

    }
}
