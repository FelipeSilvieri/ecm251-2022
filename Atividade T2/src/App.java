import java.util.ArrayList;

public class App {
    void run(){
        //criar array list de membros 
        ArrayList<Integrantes> integrantes = new ArrayList<Integrantes>();

        //Adicionando membros
        integrantes.add(new MobileMembers("Davi", "sla@outlook.com", "regular"));          //posicao 0

        integrantes.add(new HeavyLifters("Pedro", "pedro@outlook.com", "regular"));       //posicao 1   - primeiro heavy lifter
        integrantes.add(new HeavyLifters("Joao", "joao@outlook.com", "regular"));         //posicao 2

        integrantes.add(new ScriptGuys("Melissa", "melissa@outlook.com", "regular"));        //posicao 3
        integrantes.add(new ScriptGuys("Julia", "julia@outlook.com", "regular"));          //posicao 4    - segundo script guy

        integrantes.add(new BigBrothers("Ana", "anaoutlook.com@", "regular"));             //posicao 5

        printaTurnoMensagem(integrantes);

        mudaTurno(integrantes,"extra");

        printaTurnoMensagem(integrantes);

        mudaTurno(integrantes,"regular");
        
        printaTurnoMensagem(integrantes);

        integrantes.remove(1);
        integrantes.remove(3);

        printaCadastrados(integrantes);

    }
        
    public static void printaTurnoMensagem(ArrayList<Integrantes> integrantes){
        for(Integrantes item:integrantes){
            System.out.println();
            System.out.println("O turno atual de "+ item.getNome() + " é " + item.getTurno() + ". Sua mensagem é: ");
            item.postagens();
        }
    }

    public static void mudaTurno(ArrayList<Integrantes> integrantes, String turnoMudanca){
        for(Integrantes item:integrantes){
            item.MudarTurno(turnoMudanca);
        }
    }
    
    public static void printaCadastrados(ArrayList<Integrantes> integrantes){
        for(Integrantes item:integrantes){
            System.out.println(item.toString());
        }
    }

}
