public class ScriptGuys extends Integrantes{

    public ScriptGuys(String nome, String email, String turno) {
        super(nome, email, turno);
        this.funcao = "Script Guy";
    }

    @Override
    public boolean PostarMensagem() {
        if(funcao.equals("regular")){
            System.out.println("Prazer em ajudar novos amigos de código!");
            return true;
        }
        else if(funcao.equals("extra")){
            System.out.println("QU3Ro_S3us_r3curs0s.py");
            return true;
        }
        else{
            return false;
        }
        // TODO Auto-generated method stub
    }
    
}
