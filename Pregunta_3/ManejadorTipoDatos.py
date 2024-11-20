class ManejadorTipoDatos:
    almacenDeTipo = {}
    almacenDeRegistro = {}
    almacenDeRegistroVariante = {}

    # Funcion para definir un tipo de dato atómico, almacenandolo en el diccionario almacenDeTipo
    def atomico(self, entrada):
        if len(entrada) == 4:
            nombre, representacion, alineacion = entrada[1], int(entrada[2]), int(entrada[3])
            if nombre in ManejadorTipoDatos.almacenDeTipo:
                print(f"Error: El tipo '{nombre}' ya existe.")
            else:
                ManejadorTipoDatos.almacenDeTipo[nombre] = (representacion, alineacion)
        else:
            print("Error: Cantidad de argumentos incorrecta para ATOMICO.")

    # Funcion para definir un tipo de registro, almacenandolo en el diccionario almacenDeRegistro
    def struct(self, entrada):
        if len(entrada) >= 3:
            nombre, tipos = entrada[1], entrada[2:]
            if nombre in ManejadorTipoDatos.almacenDeRegistro:
                print(f"Error: El tipo '{nombre}' ya existe.")
            else:
                for tipo in tipos:
                    if tipo not in ManejadorTipoDatos.almacenDeTipo:
                        print(f"Error: El tipo '{tipo}' no está definido.")
                        return
                ManejadorTipoDatos.almacenDeRegistro[nombre] = tipos
        else:
            print("Error: Cantidad de argumentos incorrecta para STRUCT.")

    # Funcion para definir un tipo de registro variante, almacenandolo en el diccionario almacenDeRegistroVariante
    def union(self, entrada):
        if len(entrada) >= 3:
            nombre, tipos = entrada[1], entrada[2:]
            if nombre in ManejadorTipoDatos.almacenDeRegistroVariante:
                print(f"Error: El tipo '{nombre}' ya existe.")
            else:
                for tipo in tipos:
                    if tipo not in ManejadorTipoDatos.almacenDeTipo and tipo not in ManejadorTipoDatos.almacenDeRegistro:
                        print(f"Error: El tipo '{tipo}' no está definido.")
                        return
                ManejadorTipoDatos.almacenDeRegistroVariante[nombre] = tipos
        else:
            print("Error: Cantidad de argumentos incorrecta para UNION.")

    # Funcion para describir un tipo de dato, ya sea atómico, registro o registro variante
    def describir(self, entrada):
        if len(entrada) == 2:
            nombre = entrada[1]
            # Si el tipo está definido
            if nombre in ManejadorTipoDatos.almacenDeTipo:
                tamaño, aliniacion = ManejadorTipoDatos.almacenDeTipo[nombre]
                print(f"Tipo atómico '{nombre}': Tamaño = {tamaño}, Alineación = {aliniacion}, Desperdicio = 0")
            # Si el tipo es un registro
            elif nombre in ManejadorTipoDatos.almacenDeRegistro:
                tipos = ManejadorTipoDatos.almacenDeRegistro[nombre]
                self.describirStructUnion(tipos, empaquetado="STRUCT", nombre=nombre)
            # Si el tipo es un registro variante
            elif nombre in ManejadorTipoDatos.almacenDeRegistroVariante:
                tipos = ManejadorTipoDatos.almacenDeRegistroVariante[nombre]
                self.describirStructUnion(tipos, empaquetado="UNION", nombre=nombre)
            else:
                print(f"Error: El tipo '{nombre}' no está definido.")
        else:
            print("Error: Cantidad de argumentos incorrecta para DESCRIBIR.")

    # Funcion para decidir si se debe describir un registro o un registro variante
    def describirStructUnion(self, tipos, empaquetado, nombre):
        if empaquetado == "STRUCT":
            self.calcularStruct(tipos)
        elif empaquetado == "UNION":
            self.calcularUnion(tipos)

    # Funcion para calcular el tamaño, alineación y desperdicio de un registro
    def calcularStruct(self, tipos):
        # Calculando sin empaquetar, llamando a la funcion calcularTamaño
        tamaño, alineación, desperdicio = self.calcularTamaño(tipos, empaquetar=False)
        print(f"Sin empaquetar: Tamaño = {tamaño}, Alineación = {alineación}, Desperdicio = {desperdicio}")

        # Calculando empaquetado, llamando a la funcion calcularTamaño
        tamaño, alineación, desperdicio = self.calcularTamaño(tipos, empaquetar=True)
        print(f"Empaquetado: Tamaño = {tamaño}, Alineación = {alineación}, Desperdicio = {desperdicio}")

        # Reordenando los tipos de datos de mayor a menor tamaño
        tipos_reordenados = sorted(tipos, key=lambda t: ManejadorTipoDatos.almacenDeTipo[t][1], reverse=True)
        tamaño, alineación, desperdicio = self.calcularTamaño(tipos_reordenados, empaquetar=True)
        print(f"Reordenado: Tamaño = {tamaño}, Alineación = {alineación}, Desperdicio = {desperdicio}")

    # Funcion para calcular el tamaño, alineación y desperdicio de un registro variante
    def calcularUnion(self, tipos):
        # Calculando sin empaquetar, empaquetado y reordenado
        max_tamaño, max_alineación = 0, 0
        for tipo in tipos:
            tamaño, alineación = ManejadorTipoDatos.almacenDeTipo[tipo]
            max_tamaño = max(max_tamaño, tamaño)
            max_alineación = max(max_alineación, alineación)
        desperdicio = max_alineación - (max_tamaño % max_alineación) if max_tamaño % max_alineación != 0 else 0
        print(f"Sin empaquetar: Tamaño = {max_tamaño}, Alineación = {max_alineación}, Desperdicio = {desperdicio}")
        # Empaquetado (para union, empaquetado es igual a sin empaquetar)
        print(f"Empaquetado: Tamaño = {max_tamaño}, Alineación = {max_alineación}, Desperdicio = {desperdicio}")
        # Reordenado (para union, reordenado es igual a sin empaquetar)
        print(f"Reordenado: Tamaño = {max_tamaño}, Alineación = {max_alineación}, Desperdicio = {desperdicio}")

    # Funcion para calcular el tamaño, alineación y desperdicio de un registro
    def calcularTamaño(self, tipos, empaquetar):
        # Calculando el tamaño, alineación y desperdicio de un registro
        tamaño, alineación_max, offset = 0, 0, 0
        for tipo in tipos:
            tam, ali = ManejadorTipoDatos.almacenDeTipo[tipo]
            alineación_max = max(alineación_max, ali)
            if not empaquetar:
                offset = (offset + (ali - 1)) & ~(ali - 1)
            tamaño = offset + tam
            offset += tam
        desperdicio = alineación_max - (tamaño % alineación_max) if tamaño % alineación_max != 0 else 0
        return tamaño + desperdicio, alineación_max, desperdicio

# Funcion principal para leer los comandos y ejecutar las funciones correspondientes
def main():
    manejador = ManejadorTipoDatos()
    while True:
        entrada = input("$> ").strip().split()
        comando = entrada[0].upper()
        if comando == "SALIR":
            break
        elif comando == "ATOMICO":
            manejador.atomico(entrada)
        elif comando == "STRUCT":
            manejador.struct(entrada)
        elif comando == "UNION":
            manejador.union(entrada)
        elif comando == "DESCRIBIR":
            manejador.describir(entrada)
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    main()
