public class MobileMembers extends Integrantes{

    public MobileMembers(String nome, String email, String turno) {
        super(nome, email, turno);
        this.funcao = "Mobile Member";
    }

    @Override
    public boolean PostarMensagem() {
        // TODO Auto-generated method stub
        return false;
    }
    
}
