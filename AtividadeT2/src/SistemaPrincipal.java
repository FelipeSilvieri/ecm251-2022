import java.util.ArrayList;

public class SistemaPrincipal {
    void run(){
        ArrayList<Integrantes> integrantes = new ArrayList<Integrantes>();

        integrantes.add(new BigBrothers("Felipe", "felipe123@yahoo.com", "regular"));

        integrantes.add(new HeavyLifters("Roberta", "robertaalmeida@gmail.com", "regular"));

        integrantes.add(new MobileMembers("Deyverson", "deyvinho@bol.com", "regular"));

        integrantes.add(new ScriptGuys("Kleber", "kle0908@hotmail.com", "regular"));

        // Os Procedimentos:
        
        exibeMensagem(integrantes);

        trocaTurno(integrantes, "extra");

        exibeMensagem(integrantes);

        trocaTurno(integrantes, "regular");

        integrantes.remove(1); //removendo Roberta
        integrantes.remove(3); //removendo Kleber

        exibeCadastrados(integrantes);

    }
    public static void exibeMensagem(ArrayList<Integrantes> integrantes){
        for(Integrantes endereco:integrantes){
            System.out.println("O turno do(a) "+ endereco.getNome() + " é " + endereco.getTurno() + ". A Sua mensagem é a seguinte: ");
            endereco.PostarMensagem();
            System.out.println();
        }
    }

    public static void exibeCadastrados(ArrayList<Integrantes> integrantes){
        for(Integrantes endereco:integrantes){
            System.out.println(endereco.toString());
        }
    }

    public static void trocaTurno(ArrayList<Integrantes> integrantes, String turnoMudanca){
        for(Integrantes endereco:integrantes){
            endereco.MudarTurno(turnoMudanca);
        }
    }
    
    
}
