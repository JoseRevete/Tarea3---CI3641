import java.util.*;
import java.util.stream.Collectors;

class Persona {
    private final String nombre;
    private final int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public String toString() {
        return nombre + " (" + edad + " años)";
    }
}

class ConjuntoDePersonas {
    private final Set<Persona> personas;

    public ConjuntoDePersonas() {
        this.personas = new HashSet<>();
    }

    public void agregarPersona(Persona persona) {
        personas.add(persona);
    }

    public int cantidadPersonas() {
        return personas.size();
    }

    public Set<Persona> mayoresDeEdad() {
        return personas.stream()
                .filter(persona -> persona.getEdad() >= 18)
                .collect(Collectors.toSet());
    }

    public String nombreMasComun() {
        Map<String, Long> frecuencia = personas.stream()
                .collect(Collectors.groupingBy(Persona::getNombre, Collectors.counting()));

        return frecuencia.entrySet().stream()
                .max(Comparator.comparingLong(Map.Entry::getValue))
                .map(Map.Entry::getKey)
                .orElse(null);
    }
}

public class ConjuntoPersonas {
    public static void main(String[] args) {
        ConjuntoDePersonas conjunto = new ConjuntoDePersonas();

        conjunto.agregarPersona(new Persona("Ana", 20));
        conjunto.agregarPersona(new Persona("Luis", 17));
        conjunto.agregarPersona(new Persona("Ana", 22));
        conjunto.agregarPersona(new Persona("Juan", 15));
        conjunto.agregarPersona(new Persona("Luis", 18));
        conjunto.agregarPersona(new Persona("Ana", 19));

        System.out.println("Cantidad de personas: " + conjunto.cantidadPersonas());

        System.out.println("Mayores de edad:");
        conjunto.mayoresDeEdad().forEach(System.out::println);

        System.out.println("Nombre más común: " + conjunto.nombreMasComun());
    }
}
