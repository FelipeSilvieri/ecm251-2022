import java.time.LocalDate;

public class Titulo {
    private double valor;
    private LocalDate data;
    //Precisamos de uma data
    private double multaDiaria;
    
    public Titulo(double valor, LocalDate data, double multaDiaria){
        this.Valor(valor);
        this.Data(data);
        this.MultaDiaria(multaDiaria);
    }

    public double getMultaDiaria() {
        return multaDiaria;
    }

    public LocalDate getData() {
        return data;
    }

    public double getValor() {
        return valor;
    }


    
}
