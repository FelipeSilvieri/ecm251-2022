import java.util.ArrayList;

public class SistemaPrincipal {
    void run(){
        ArrayList<Integrantes> integrantes = new ArrayList<Integrantes>();

        integrantes.add(new BigBrothers("Felipe", "felipe123@yahoo.com", "regular"));

        integrantes.add(new HeavyLifters("Roberta", "robertaalmeida@gmail.com", "regular"));

        integrantes.add(new MobileMembers("Deyverson", "deyvinho@bol.com", "regular"));

        integrantes.add(new ScriptGuys("Kleber", "kle0908@hotmail.com", "regular"));
    }
    
}
