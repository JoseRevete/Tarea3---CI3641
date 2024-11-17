abstract class Church {
    
    abstract Church suma(Church n);
    abstract Church multiplicacion(Church n);
    abstract int valor();
}

class Zero extends Church {
    
    Church suma(Church n) {
        return n;
    }
    
    Church multiplicacion(Church n) {
        return new Zero();
    }
    
    int valor() {
        return 0;
    }
}

class Suc extends Church {
    
    Church n;
    
    Suc(Church n) {
        this.n = n;
    }
    
    Church suma(Church n) {
        return new Suc(this.n.suma(n));
    }
    
    Church multiplicacion(Church n) {
        return this.n.multiplicacion(n).suma(n);
    }
    
    int valor() {
        return 1 + this.n.valor();
    }
}

public class Churchs {
    
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
        
        Church suma = cinco.suma(tres);
        Church multiplicacion = cinco.multiplicacion(tres);
        
        System.out.println("Suma de cinco y tres: "+suma.valor());
        System.out.println("Multiplicacion de cinco y tres: "+multiplicacion.valor());
    }
}