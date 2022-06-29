public class BigBrothers extends Integrantes{

    public BigBrothers(String nome, String email, String turno) {
        super(nome, email, turno);
        this.funcao = "Big Brother";
    }

    @Override
    public boolean PostarMensagem() {
        if(turno.equals("regular")){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
            return true;
        }
        else if(turno.equals("extra")){
            System.out.println("... ");
            return true;
        }
        else{
            return false;
        }
        // TODO Auto-generated method stub
        
    }
    
}
