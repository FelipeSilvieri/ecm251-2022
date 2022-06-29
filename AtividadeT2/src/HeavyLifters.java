public class HeavyLifters extends Integrantes{

    public HeavyLifters(String nome, String email, String turno) {
        super(nome, email, turno);
        this.funcao = "Heavy Lifter";
    }

    @Override
    public boolean PostarMensagem() {
        if(turno.equals("regular")){
            System.out.println("Podem contar conosco!");
            return true;
        }
        else if(turno.equals("extra")){
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
            return true;
        }
        else{
            return false;
        }
        // TODO Auto-generated method stub
    }
    
}
