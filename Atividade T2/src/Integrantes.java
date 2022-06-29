public abstract class Integrantes implements Interface{

    private String nome;
    private String email;
    protected String funcao;
    protected String turno;

    
    public Integrantes(String nome, String email, String turno) {
        this.nome = nome;
        this.email = email;
        this.turno = turno;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getTurno() {
        return turno;
    }

    public String getFuncao() {
        return funcao;
    }
  
    @Override
    public void MudarTurno(String turnoDepois) {
        turno = turnoDepois;
    }

    @Override
    public String toString() {
        return "Integrantes [email=" + email + ", funcao=" + funcao + ", nome=" + nome + ", turno=" + turno + "]";
    }

}

