// Clase Church para representar los numeros naturales con funciones
abstract class Church {
    abstract Church suma(Church n);
    abstract Church multiplicacion(Church n);
    abstract int valor();
}

// Clase Zero que representa el cero
class Zero extends Church {
    Church suma(Church n) {return n;}
    Church multiplicacion(Church n) {return new Zero();}
    int valor() {return 0;}
}

// Clase Suc que representa el sucesor de un numero
class Suc extends Church {
    Church n;
    Suc(Church n) {this.n = n;}
    Church suma(Church n) {return new Suc(this.n.suma(n));}
    Church multiplicacion(Church n) {return this.n.multiplicacion(n).suma(n);}
    int valor() {return 1 + this.n.valor();}
}

// Clase Churchs que contiene el metodo main
public class Churchs {
    // Metodo main
    public static void main(String[] args) {
        Church cero = new Zero();
        Church uno = new Suc(cero);
        Church dos = new Suc(uno);
        Church tres = new Suc(dos);
        Church cuatro = new Suc(tres);
        Church cinco = new Suc(cuatro);
        
        System.out.println("Valor de cero: "+cero.valor());
        System.out.println("Valor de uno: "+uno.valor());
        System.out.println("Valor de dos: "+dos.valor());
        System.out.println("Valor de tres: "+tres.valor());
        System.out.println("Valor de cuatro: "+cuatro.valor());
        System.out.println("Valor de cinco: "+cinco.valor());
        
        Church ocho = cinco.suma(tres);
        Church diez = ocho.suma(dos);
        Church multiplicacion = cinco.multiplicacion(tres);
        
        System.out.println("Suma de ocho y dos: "+diez.valor());
        System.out.println("Multiplicacion de cinco y tres: "+multiplicacion.valor());
    }
}