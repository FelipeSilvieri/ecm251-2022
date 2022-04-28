import java.util.concurrent.ThreadLocalRandom;

public class Usuario {
    public Usuario(String nome){
        this.nome = nome;
    }
    
    public int id;
    public void gerarId(int id){
        this.id = id;
        id = ThreadLocalRandom.current().nextInt(10000, 99999);
    }        
    public void testar(int id, string tipo) {
        
    }
