# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero ahora usamos lo que Python
#  ya trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, next, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  ✅ OBLIGATORIO usar comprensiones de listas en (mínimo):
#       buscar · buscar_binaria · eliminar_por_valor (versión 2)
#       filtrar_mayores_de_edad · nombres_en_mayusculas
#
#  Recordatorio de la sintaxis:
#       [EXPRESIÓN for ELEMENTO in LISTA]            -> transformar
#       [ELEMENTO  for ELEMENTO in LISTA if COND]    -> filtrar
#       [EXPRESIÓN for ELEMENTO in LISTA if COND]    -> las dos a la vez
#
#  📌 Compara cada método con su gemelo de lista_manual.py:
#     allá eran 10 líneas, aquí casi siempre son 1 o 2.
#  Cuando termines un método, BORRA la línea "pass".
# =====================================================================

from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:

    def __init__(self):
        self.pasajeros = []               # list de Python: crece sola

    # -----------------------------------------------------------------
    # 1. AÑADIR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False
        """Añade al final con append()."""
        self.pasajeros.append(pasajero)
        return True
        # 🔧 MEJORA cuando termines buscar(): no añadir cédulas repetidas.

    # -----------------------------------------------------------------
    # 2. LISTAR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        if not self.pasajeros:                  # lista vacía es False
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        return len(self.pasajeros)
        """
        USA      : len()
        RETORNA  : int.   PRUEBA: datos de prueba -> 5
        """
        

    # -----------------------------------------------------------------
    # 4. INSERTAR
    # -----------------------------------------------------------------
    def insert(self, pos, p):
        if 0 <= pos <= len(self.pasajeros):
            self.pasajeros.insert(pos, p)
            return True
        else:   
            print("Posición inválida")
            return False
        """
        USA      : self.pasajeros.insert(posicion, pasajero)
        VALIDA   : 0 <= posicion <= len(self.pasajeros); si no, mensaje y False.
        PIENSA   : ¿por qué ya no tienes que correr nada a la derecha?
                   (Python lo hace por ti... pero lo sigue haciendo: O(n)).
        """
        

    # -----------------------------------------------------------------
    # 5. BUSCAR POR CÉDULA  (con COMPRENSIÓN)
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        if not posiciones:
            return -1    
        return posiciones[0]
     
    #def buscar(self, cedula):
    #    return next((i for i, p in enumerate(self.pasajeros) if p.cedula == cedula), -1) 
    
        """
        RETORNA  : la posición (int) o -1.
        USA      : una comprensión con enumerate que junte las posiciones
                   que coinciden:
                       posiciones = [i for i, p in enumerate(self.pasajeros)
                                     if p.cedula == cedula]
                   Si la lista 'posiciones' está vacía -> -1,
                   si no -> posiciones[0].
        EXTRA    : investiga la versión con next(...):
                   next((i for i, p in enumerate(...) if ...), -1)
        PRUEBA   : buscar("0987654321") -> 2 ;  buscar("1111111111") -> -1
        """
        

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA  (con COMPRENSIÓN + bisect)
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        self.ordenar_asc()
        cedulas = [p.cedula for p in self.pasajeros]
        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1
        """
        ⚠ REQUISITO: lista ordenada por cédula (ordenar_asc antes).
        PASOS    :
          1. cedulas = [p.cedula for p in self.pasajeros]   # COMPRENSIÓN
          2. i = bisect_left(cedulas, cedula)   # dónde "debería" estar
          3. Si i < len(cedulas) y cedulas[i] == cedula -> return i
          4. return -1
        PRUEBA   : datos ordenados -> buscar_binaria("0923456789") -> 2
        """
        

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True
        """
        PASOS    : pos = self.buscar(cedula); si -1 -> False;
                   si no, cambia self.pasajeros[pos].nombre y .edad -> True
        """
        

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, pos):
        if 0 <= pos < len(self.pasajeros):
            return self.pasajeros.pop(pos)
        else:
            print("Posición inválida")
            return None
        """
        USA      : self.pasajeros.pop(posicion)   (retorna el eliminado)
        VALIDA   : 0 <= posicion < len(...); si no -> mensaje y None
        """
        

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)  — hazlo de DOS formas
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        #forma 1 (remove):
        #pos = self.buscar(cedula)
        #if pos == -1:
        #    return False
        #self.pasajeros.remove(self.pasajeros[pos])
        #return True 
        

        #forma 2 (comprensión):
        antes = len(self.pasajeros) 
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        return len(self.pasajeros) < antes      
        """
        FORMA 1 (remove):
            pos = self.buscar(cedula) ... self.pasajeros.remove(self.pasajeros[pos])
        FORMA 2 (COMPRENSIÓN) — la que debe quedar activa:
            antes = len(self.pasajeros)
            self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
            return len(self.pasajeros) < antes      # True si eliminó algo
        Deja la FORMA 1 comentada para comparar.
        """
        

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.cedula)
        """
        USA      : self.pasajeros.sort(key=lambda p: p.cedula)
        PIENSA   : ¿qué hace key=? ¿qué pasaría sin él? (pruébalo)
        Le indica al método .sort() qué criterio o atributo específico de cada elemento debe extraer para realizar las comparaciones. 
        La función anónima lambda p: p.cedula toma cada objeto p (un pasajero) y extrae su atributo .cedula.
        """
        

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)
        """ USA : sort(key=..., reverse=True) """
        

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        self.pasajeros.reverse()
        """ USA : self.pasajeros.reverse()   (no es lo mismo que ordenar_desc) """
        

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva
        """
        PASOS    :
          nueva = ListaPasajerosPython()
          nueva.pasajeros = self.pasajeros.copy()    # o self.pasajeros[:]
          return nueva
        ⚠ OJO    : es una copia SUPERFICIAL: las dos listas son distintas,
                   pero los objetos Pasajero de adentro son los MISMOS.
                   Reversar la copia no afecta al original;
                   modificar un pasajero de la copia... ¡sí! Pruébalo.
        """
        

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD  (COMPRENSIÓN que FILTRA)
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva
        """
        RETORNA  : una NUEVA ListaPasajerosPython.
        PASOS    :
          nueva = ListaPasajerosPython()
          nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
          return nueva
        PRUEBA   : datos de prueba -> todos menos Beto
        """
        

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS  (COMPRENSIÓN que TRANSFORMA)
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        return [p.nombre.upper() for p in self.pasajeros]
        """
        RETORNA  : list de str ->  [p.nombre.upper() for p in self.pasajeros]
        PRUEBA   : ['DIANA', 'ANA', 'LUIS', 'BETO', 'ELENA']
        """


if __name__ == "__main__":
    # Instanciación
    lista = ListaPasajerosPython()

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
    lista.insert(1, Pasajero("Carlos", "0999999999", 30))
    lista.listar()

    # 5. Buscar por comprensión
    print("\n--- 5. Buscar '0987654321' ---")
    pos = lista.buscar("0987654321")
    print(f"Encontrado en índice: {pos}")

    # 7. Modificar
    print("\n--- 7. Modificar '0934567890' -> Roberto (17 años) ---")
    lista.modificar("0934567890", "Roberto", 17)
    lista.listar()

    # 8. Eliminar por posición
    print("\n--- 8. Eliminar por posición 1 ---")
    eliminado = lista.eliminar_por_posicion(1)
    print(f"Eliminado: {eliminado}")

    # 9. Eliminar por valor (comprensión)
    print("\n--- 9. Eliminar por cédula '0987654321' ---")
    lista.eliminar_por_valor("0987654321")
    lista.listar()

    # 10. Ordenar Ascendente
    print("\n--- 10. Ordenar Ascendente ---")
    lista.ordenar_asc()
    lista.listar()

    # 6. Buscar Binaria
    print("\n--- 6. Buscar Binaria '0912345678' ---")
    pos_bin = lista.buscar_binaria("0912345678")
    print(f"Encontrado en índice: {pos_bin}")

    # 11. Ordenar Descendente
    print("\n--- 11. Ordenar Descendente ---")
    lista.ordenar_desc()
    lista.listar()

    # 12. Reversar
    print("\n--- 12. Reversar ---")
    lista.reversar()
    lista.listar()

    # 13. Copiar
    print("\n--- 13. Copiar y reversar copia ---")
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