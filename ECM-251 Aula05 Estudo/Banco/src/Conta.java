public class Conta {
    //Atributos da nossa Classe
    int numero;
    string titular;
    float saldo;
    string cpf;

    void visualizarSaldo(){
        System.out.println("O saldo na conta " + numero + " é de R$: " + saldo );
    }

}
