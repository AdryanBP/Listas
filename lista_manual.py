# =====================================================================
#  lista_manual.py  —  LISTA 1: construida DESDE CERO (como MiLista)
# ---------------------------------------------------------------------
#  Esta clase imita la clase MiLista del módulo 7 de la guía.
#  Por dentro hay un ARREGLO de tamaño fijo con cajones vacíos (None).
#
#      datos     -> [Ana, Beto, Carlos, None, None, ...]
#      capacidad -> cuántos cajones hay en total          (10)
#      cantidad  -> cuántos cajones están ocupados        (3)
#
#  LAS DOS REGLAS QUE EXPLICAN TODA LA CLASE
#    1. Los pasajeros van SEGUIDOS: de datos[0] a datos[cantidad-1].
#       No puede haber huecos (None) en medio.
#    2. Para INSERTAR se corre a la DERECHA (de atrás hacia adelante).
#       Para ELIMINAR se corre a la IZQUIERDA (de adelante hacia atrás).
#
#  ⛔ PROHIBIDO en esta clase (aquí se trabaja "a mano"):
#     append, insert, pop, remove, index, sort, sorted, reverse,
#     reversed, copy, len(), el operador "x in lista" para buscar,
#     slicing [a:b] ni comprensiones.  (for i in range(...) SÍ se puede)
#  ✅ PERMITIDO: índices datos[i], while, for i in range(...), if,
#     variables auxiliares (aux), y self.cantidad / self.capacidad.
#
#  📌 Método de trabajo para CADA método (el método de 5 pasos):
#     1) Entrada / Proceso / Salida   2) Bosquejo a mano con datos
#     3) Descubrir el patrón          4) Escribir el código
#     5) Prueba de escritorio
#
#  Cuando termines un método, BORRA la línea "pass".
# =====================================================================

from pasajero import Pasajero


class ListaPasajerosManual:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad   # los "cajones"
        self.capacidad = capacidad        # cuántos cajones hay
        self.cantidad = 0                 # cuántos están ocupados

    # -----------------------------------------------------------------
    # 1. AÑADIR  ✅ YA RESUELTO (úsalo como modelo)
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Pone el pasajero en el primer cajón libre (al final)."""
        if self.cantidad == self.capacidad:
            print("⚠ La lista está llena")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False
        # El primer cajón libre SIEMPRE es datos[cantidad]
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True
        # 🔧 MEJORA cuando termines buscar(): antes de añadir, verifica
        #    que la cédula no exista:  if self.buscar(pasajero.cedula) != -1

    # -----------------------------------------------------------------
    # 2. LISTAR  ✅ YA RESUELTO (úsalo como modelo)
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición."""
        if self.cantidad == 0:
            print("(lista vacía)")
            return
        for i in range(self.cantidad):          # solo los cajones ocupados
            print(f"[{i}] {self.datos[i]}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        return self.cantidad
        """
        QUÉ HACE : retorna cuántos pasajeros hay.
        CÓMO     : no recorras nada; el dato ya está guardado en un atributo.
        RETORNA  : int
        PRUEBA   : con los 5 pasajeros de prueba -> 5
        """


    # -----------------------------------------------------------------
    # 4. INSERTAR EN UNA POSICIÓN
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return False
        i = self.cantidad                   # empiezo por el final
        while i > posicion:
            self.datos[i] = self.datos[i - 1]   # muevo cada uno un lugar a la derecha
            i = i - 1
        self.datos[posicion] = pasajero        # el nuevo entra en el hueco
        self.cantidad = self.cantidad + 1
        return True
        """
        QUÉ HACE : mete el pasajero en 'posicion' corriendo los demás
                   un lugar a la DERECHA.
        PASOS    :
          1. Si la lista está llena -> mensaje y return False.
          2. Si posicion < 0 o posicion > cantidad -> "Posición no válida",
             return False.  (posicion == cantidad SÍ es válida: es el final)
          3. i = self.cantidad   (empiezo por el ÚLTIMO cajón libre)
          4. Mientras i > posicion:
                 datos[i] = datos[i - 1]     # muevo uno a la derecha
                 i = i - 1
          5. datos[posicion] = pasajero      # el nuevo entra en el hueco
          6. cantidad + 1  y  return True
        OJO      : si recorres de adelante hacia atrás, PISAS los datos.
        PRUEBA   : [Diana, Ana, Luis] -> insertar(1, Xavi)
                   -> [Diana, Xavi, Ana, Luis]
        """
        

    # -----------------------------------------------------------------
    # 5. BUSCAR (LINEAL) POR CÉDULA
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        for i in range(self.cantidad):
            if self.datos[i].cedula == cedula:
                return i
        return -1
        """
        QUÉ HACE : busca un pasajero por cédula revisando uno por uno.
        PATRÓN   : 🔴 búsqueda lineal (módulo 0).
        PASOS    :
          1. Recorre i desde 0 hasta cantidad - 1.
          2. Si datos[i].cedula == cedula -> return i
          3. Si terminas el recorrido sin encontrarlo -> return -1
        RETORNA  : la POSICIÓN (int) o -1 si no existe.
        PRUEBA   : buscar("0987654321") con datos de prueba -> 2
                   buscar("1111111111")                     -> -1
        """
    

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA POR CÉDULA
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].cedula == cedula:
                return medio                # lo encontré
            elif self.datos[medio].cedula < cedula:
                izq = medio + 1             # está a la derecha
            else:
                der = medio - 1             # está a la izquierda
        return -1                           # no está
        """
        QUÉ HACE : busca partiendo la lista por la mitad.
        ⚠ REQUISITO: la lista DEBE estar ordenada por cédula
                     (llama antes a ordenar_asc()).
        PASOS    :
          1. izq = 0 ; der = cantidad - 1
          2. Mientras izq <= der:
                 medio = (izq + der) // 2
                 si datos[medio].cedula == cedula -> return medio
                 si datos[medio].cedula <  cedula -> izq = medio + 1
                 si no                            -> der = medio - 1
          3. return -1
        NOTA     : las cédulas son str; "0901..." < "0912..." funciona
                   porque todas tienen 10 dígitos.
        PRUEBA   : datos de prueba ORDENADOS -> buscar_binaria("0923456789") -> 2
        """

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            print(cedula, "no existe")
            return False
        self.datos[pos].nombre = nuevo_nombre
        self.datos[pos].edad = nueva_edad
        return True
        """
        QUÉ HACE : cambia nombre y edad del pasajero con esa cédula.
        PASOS    :
          1. pos = self.buscar(cedula)          # REUTILIZA buscar
          2. Si pos == -1 -> mensaje "no existe" y return False
          3. datos[pos].nombre = nuevo_nombre
             datos[pos].edad   = nueva_edad
          4. return True
        PRUEBA   : modificar("0934567890", "Roberto", 17) -> Beto pasa a Roberto
        """

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None
        valor = self.datos[posicion]        # guardo el que voy a quitar
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]   # muevo cada uno un lugar a la izquierda
        self.datos[self.cantidad - 1] = None    # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return valor
        """
        QUÉ HACE : quita el pasajero de esa posición y lo RETORNA.
        PASOS    :
          1. Si posicion < 0 o posicion >= cantidad -> mensaje y return None
          2. valor = datos[posicion]             # guardo el que voy a quitar
          3. for i in range(posicion, cantidad - 1):
                 datos[i] = datos[i + 1]         # corro a la IZQUIERDA
          4. datos[cantidad - 1] = None          # el último cajón queda vacío
          5. cantidad - 1
          6. return valor
        PRUEBA   : datos de prueba -> eliminar_por_posicion(0) retorna a Diana
                   y la lista queda [Ana, Luis, Beto, Elena]
        """


    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        pos = self.buscar(cedula)
        if pos == -1:
            print(cedula, "no existe")
            return False
        self.eliminar_por_posicion(pos)
        return True
        """
        QUÉ HACE : quita el pasajero que tenga esa cédula.
        PASOS    : son DOS métodos que ya tienes:
          1. pos = self.buscar(cedula)
          2. Si pos == -1 -> mensaje y return False
          3. self.eliminar_por_posicion(pos)  y  return True
        IDEA     : no repitas el código de correr a la izquierda; REUTILIZA.
        PRUEBA   : eliminar_por_valor("0987654321") -> Luis desaparece
        """

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula) — MÉTODO BURBUJA
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula > self.datos[i + 1].cedula:
                    aux = self.datos[i]                 # intercambio con
                    self.datos[i] = self.datos[i + 1]   # una variable
                    self.datos[i + 1] = aux             # auxiliar

        """
        QUÉ HACE : ordena de menor a mayor cédula.
        PASOS    :
          n = cantidad
          for vuelta in range(n - 1):
              for i in range(n - 1 - vuelta):
                  si datos[i].cedula > datos[i + 1].cedula:
                      aux = datos[i]               # intercambio con
                      datos[i] = datos[i + 1]      # variable auxiliar
                      datos[i + 1] = aux
        PRUEBA   : datos de prueba -> Elena, Ana, Diana, Beto, Luis
        """


    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula < self.datos[i + 1].cedula:
                    aux = self.datos[i]                 # intercambio con
                    self.datos[i] = self.datos[i + 1]   # una variable
                    self.datos[i + 1] = aux             # auxiliar

        """
        QUÉ HACE : ordena de MAYOR a menor cédula.
        CÓMO     : copia la burbuja de ordenar_asc y cambia UN solo
                   símbolo de la comparación. ¿Cuál? Descúbrelo en el bosquejo.
        PRUEBA   : datos de prueba -> Luis, Beto, Diana, Ana, Elena
        """
        

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1
        """
        QUÉ HACE : invierte el orden (el primero pasa a ser el último).
        PASOS    : dos punteros que se acercan:
          izq = 0 ; der = cantidad - 1
          mientras izq < der:
              intercambia datos[izq] y datos[der] (con aux)
              izq + 1 ; der - 1
        PRUEBA   : [Diana, Ana, Luis, Beto, Elena] -> [Elena, Beto, Luis, Ana, Diana]
        """


    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        nueva = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva
        """
        QUÉ HACE : crea OTRA ListaPasajerosManual con los mismos pasajeros.
        PASOS    :
          1. nueva = ListaPasajerosManual(self.capacidad)
          2. for i in range(self.cantidad): nueva.añadir(self.datos[i])
          3. return nueva
        PRUEBA   : copia = lista.copiar(); copia.reversar()
                   -> la copia cambia de orden, la ORIGINAL NO.
        """


    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD (versión manual de una "comprensión")
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        resultado = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            if self.datos[i].es_mayor_de_edad():
                resultado.añadir(self.datos[i])
        return resultado
        """
        QUÉ HACE : retorna una NUEVA ListaPasajerosManual solo con los
                   pasajeros de 18 años o más. La original no cambia.
        PATRÓN   : recorrer + if + añadir a otra lista.
        PASOS    :
          1. resultado = ListaPasajerosManual(self.capacidad)
          2. recorre i en range(cantidad):
                 si datos[i].es_mayor_de_edad(): resultado.añadir(datos[i])
          3. return resultado
        COMPARA  : en la Lista 2 esto será UNA línea con comprensión.
        PRUEBA   : datos de prueba -> todos menos Beto (16 años)
        """
        

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS (versión manual de una "comprensión")
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        resultado = [None] * self.cantidad
        for i in range(self.cantidad):
            resultado[i] = self.datos[i].nombre.upper()
        return resultado
        """
        QUÉ HACE : retorna un arreglo con los NOMBRES en mayúsculas
                   (transformar). La lista original no cambia.
        PASOS    :
          1. resultado = [None] * self.cantidad     # arreglo del tamaño justo
          2. for i in range(cantidad):
                 resultado[i] = datos[i].nombre.upper()
          3. return resultado
        PRUEBA   : datos de prueba -> ['DIANA', 'ANA', 'LUIS', 'BETO', 'ELENA']
        """

if __name__ == "__main__":
    
    # Instanciación
    lista = ListaPasajerosManual(capacidad=10)

    # 1. Añadir
    print("\n--- 1. Añadir pasajeros ---")
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    lista.añadir(Pasajero("Beto",  "0934567890", 16))
    lista.añadir(Pasajero("Elena", "0901234567", 41))

    # 2. Listar
    print("\n--- 2. Listar ---")
    lista.listar()

    # 3. Longitud
    print(f"\n--- 3. Longitud: {lista.longitud()} ---")

    # 4. Insertar
    print("\n--- 4. Insertar en posición 1 (Carlos) ---")
    lista.insertar(1, Pasajero("Carlos", "0999999999", 30))
    lista.listar()

    # 5. Buscar (lineal)
    print("\n--- 5. Buscar '0987654321' ---")
    pos = lista.buscar("0987654321")
    print(f"Encontrado en índice: {pos}")

    # 6. Modificar
    print("\n--- 6. Modificar '0934567890' -> Roberto (17 años) ---")
    lista.modificar("0934567890", "Roberto", 17)
    lista.listar()

    # 7. Eliminar por posición
    print("\n--- 7. Eliminar en posición 1 ---")
    eliminado = lista.eliminar_por_posicion(1)
    print(f"Eliminado: {eliminado}")

    # 8. Eliminar por valor (cédula)
    print("\n--- 8. Eliminar por cédula '0987654321' ---")
    lista.eliminar_por_valor("0987654321")
    lista.listar()

    # 9. Ordenar Ascendente
    print("\n--- 9. Ordenar Ascendente ---")
    lista.ordenar_asc()
    lista.listar()

    # 6. Buscar Binaria
    print("\n--- 6. Buscar Binaria '0912345678' ---")
    pos_bin = lista.buscar_binaria("0912345678")
    print(f"Encontrado en índice: {pos_bin}")

    # 10. Ordenar Descendente
    print("\n--- 10. Ordenar Descendente ---")
    lista.ordenar_desc()
    lista.listar()

    # 11. Reversar
    print("\n--- 11. Reversar ---")
    lista.reversar()
    lista.listar()

    # 12. Copiar
    print("\n--- 12. Copiar y reversar copia ---")
    copia = lista.copiar()
    copia.reversar()
    print("Copia:")
    copia.listar()
    print("Original (no cambia):")
    lista.listar()

    # 14. Filtrar mayores de edad
    print("\n--- 14. Mayores de edad ---")
    mayores = lista.filtrar_mayores_de_edad()
    mayores.listar()

    # 15. Nombres en mayúsculas
    print("\n--- 15. Nombres en mayúsculas ---")
    print(lista.nombres_en_mayusculas())