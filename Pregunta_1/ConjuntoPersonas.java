import java.util.*;
import java.util.stream.Collectors;

// Clase que representa un conjunto de personas, donde cada persona tiene un nombre y una edad.
public class ConjuntoPersonas {
    // Lista de pares (nombre, edad) de las personas en el conjunto
    private final List<Map.Entry<String, Integer>> personas;

    // Constructor de la clase
    public ConjuntoPersonas(List<Map.Entry<String, Integer>> personas) {this.personas = personas;}

    // Metodo que retorna la cantidad de personas en el conjunto
    public int cantidadPersonas() {return personas.size();}

    // Metodo que retorna una lista con las personas mayores de edad
    public List<Map.Entry<String, Integer>> mayoresDeEdad() {
        return personas.stream()
                .filter(entry -> entry.getValue() >= 18)
                .collect(Collectors.toList());
    }

    // Metodo que retorna el nombre más común en el conjunto
    public String nombreMasComun() {
        Map<String, Long> frecuencia = new HashMap<>();
        for (Map.Entry<String, Integer> persona : personas) {
            String nombre = persona.getKey();
            frecuencia.put(nombre, frecuencia.getOrDefault(nombre, 0L) + 1);
        }
        String nombreMasComun = null;
        long maxFrecuencia = 0;
        for (Map.Entry<String, Long> entrada : frecuencia.entrySet()) {
            if (entrada.getValue() > maxFrecuencia) {
                nombreMasComun = entrada.getKey();
                maxFrecuencia = entrada.getValue();
            }
        }
        return nombreMasComun;
    }

    // Metodo main
    public static void main(String[] args) {
        List<Map.Entry<String, Integer>> personas = new ArrayList<>(Arrays.asList(
            new AbstractMap.SimpleEntry<>("Ana", 20),
            new AbstractMap.SimpleEntry<>("Luis", 17),
            new AbstractMap.SimpleEntry<>("Ana", 22),
            new AbstractMap.SimpleEntry<>("Juan", 15),
            new AbstractMap.SimpleEntry<>("Luis", 18),
            new AbstractMap.SimpleEntry<>("Ana", 19)
        ));

        ConjuntoPersonas conjunto = new ConjuntoPersonas(personas);

        System.out.println("Cantidad de personas: " + conjunto.cantidadPersonas());

        System.out.println("Mayores de edad:");
        conjunto.mayoresDeEdad().forEach(entry -> 
            System.out.println(entry.getKey() + " (" + entry.getValue() + " años)")
        );

        System.out.println("Nombre más común: " + conjunto.nombreMasComun());
    }
}