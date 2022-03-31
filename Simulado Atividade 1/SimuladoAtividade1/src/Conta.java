// Nome: Felipe Matos Silvieri
// RA: 20.00314-5


public class Conta {
    private int idConta;
    private double saldo;
    private string nome;

    public Conta(int idConta, double saldo, string nome){
        this.idConta = idConta;
        this.nome = nome;
        saldo = 0;

    }
   
    //Métodos da classe
    public String visualizarSaldo(){
        return String.format("R$%.2f", saldo);
    }
    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Numero:"+numero 
        + "\nCliente:" + cliente.getNome()
        + "\nSaldo:" + visualizarSaldo();
    }
}

