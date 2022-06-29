public class MobileMembers extends Integrantes{

    public MobileMembers(String nome, String email, String turno) {
        super(nome, email, turno);
        this.funcao = "Mobile Member";
    }

    @Override
    public boolean PostarMensagem() {
        if(funcao.equals("regular")){
            System.out.println("Happy Coding!");
            return true;
        }
        else if(funcao.equals("extra")){
            System.out.println("Happy_C0d1ng. Maskers");
            return true;
        }
        else{
            return false;
        }
        // TODO Auto-generated method stub
    }
    
}
