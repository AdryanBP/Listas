def ejercicio_t1():
    class Pasajero:
        def __init__(self, nombre, cedula):
            self.nombre = nombre
            self.cedula = cedula

        def __str__(self):
            return f"{self.nombre} ({self.cedula})"


    def buscar_por_cedula(lista, ced):
        """Retorna el objeto o None."""
        return next((p for p in lista if p.cedula == ced), None)


    # --- Programa principal ---
    lista = []

    while True:
        print("\n--- MENÚ ---")
        print("1.Agregar\n 2.Listar\n 3.Buscar\n 4.Modificar\n 5.Eliminar\n 6.Salir")
        op = input("Opción: ")

        if op == "1":
            nom = input("Nombre: ")
            ced = input("Cédula: ")
            if buscar_por_cedula(lista, ced):
                print("Ya existe un pasajero con esa cédula")
            else:
                lista.append(Pasajero(nom, ced))
                print("Agregado ✓")

        elif op == "2":
            if not lista:
                print("No hay pasajeros")
            for i, p in enumerate(lista):
                print(f"[{i}] {p}")

        elif op == "3":
            ced = input("Cédula: ")
            p = buscar_por_cedula(lista, ced)
            print(p if p else "No existe")

        elif op == "4":
            ced = input("Cédula: ")
            p = buscar_por_cedula(lista, ced)
            if p:
                p.nombre = input("Nuevo nombre: ")
                print("Modificado ✓")
            else:
                print("No existe")

        elif op == "5":
            ced = input("Cédula: ")
            p = buscar_por_cedula(lista, ced)
            if p:
                lista.remove(p)
                print("Eliminado ✓")
            else:
                print("No existe")

        elif op == "6":
            break


def ejercicio_t2():
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas   = [ 8,     6,      10,      7,      5]

    # Python trae todo esto:
    print(f"Promedio: {sum(notas) / len(notas):.2f}")
    print(f"Máxima: {max(notas)}")
    print(f"Mínima: {min(notas)}")

    # Aprobados: filtro + len
    aprobados = [n for n in notas if n >= 7]
    print(f"Aprobados: {len(aprobados)} de {len(notas)}")

    # Mejor estudiante: índice del máximo
    idx_max = notas.index(max(notas))
    print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

    # --- Versión manual (para entender qué hace por dentro) ---
    suma = 0
    maxima = notas[0]
    minima = notas[0]
    idx_max_manual = 0
    aprob_manual = 0

    for i in range(len(notas)):
        suma += notas[i]
        if notas[i] > maxima:
            maxima = notas[i]
            idx_max_manual = i
        if notas[i] < minima:
            minima = notas[i]
        if notas[i] >= 7:
            aprob_manual += 1

    print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")


def ejercicio_t3():
    def bubble_sort(lista):
        n = len(lista)
        # Copia para no modificar el original
        arr = lista[:]
        for vuelta in range(n - 1):
            # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
            hubo_swap = False
            for i in range(n - 1 - vuelta):
                if arr[i] > arr[i + 1]:
                    # Intercambio en una línea
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    hubo_swap = True
            if not hubo_swap:
                break
        return arr


    # --- Uso ---
    notas = [5, 2, 8, 1, 9, 3, 7]

    # Nuestra versión
    ordenada = bubble_sort(notas)
    print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

    # La versión de Python (usa Timsort, mucho más rápido)
    copia = notas[:]                           # copia para no romper el original
    copia.sort()
    print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

    # Descendente
    copia.sort(reverse=True)
    print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

    # Ordenar por criterio (ej. por longitud del string)
    palabras = ["python", "a", "código", "el"]
    palabras.sort(key=len)
    print(palabras)                            # ['a', 'el', 'python', 'código']


# ============================= PROPUESTOS ============================

def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3

    # Manual
    count = 0
    for x in lista:
        if x == v:
            count += 1
    print(f"{v} aparece {count} veces")

    # Pythonic
    print(f"{v} aparece {lista.count(v)} veces")


def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    lista = [1, 2, 3, 4, 5]

    # Con bucle
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print(invertida)

    # Con slicing (pythonic)
    print(lista[::-1])

    # Con reversed
    print(list(reversed(lista)))


def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
               NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    nums = [1, 3, 2, 3, 4, 1, 5, 2]

    # Manual (mantiene orden)
    unicos = []
    for x in nums:
        if x not in unicos:
            unicos.append(x)
    print(unicos)                       # [1, 3, 2, 4, 5]

    # Rápido (NO mantiene orden)
    print(list(set(nums)))

    # Rápido MANTENIENDO orden (Python 3.7+)
    print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]


def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    nums = [5, 2, 9, 7, 9, 3, 8]

    # Dos campeones: mayor y segundo
    mayor = float("-inf")
    segundo = float("-inf")

    for n in nums:
        if n > mayor:
            segundo = mayor         # el que era mayor pasa a segundo
            mayor = n
        elif n > segundo and n < mayor:
            segundo = n

    print(f"Mayor: {mayor}")
    print(f"Segundo: {segundo}")


def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
               y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]

    resultado = []
    i = j = 0

    # Recorremos las dos listas a la par
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    # Añadimos lo que quede de la más larga
    resultado.extend(a[i:])
    resultado.extend(b[j:])

    print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]


# =====================================================================
#  PRUEBA INDIVIDUAL DE EJERCICIOS (ejercicios.py)
# =====================================================================
if __name__ == "__main__":
    print("==========================================")
    print("      PRUEBA DE EJERCICIOS (Taller)       ")
    print("==========================================")

    print("\n--- T1: CRUD Pasajero con menú ---")
    ejercicio_t1()

    print("\n--- T2: Estadísticas de notas ---")
    ejercicio_t2()

    print("\n--- T3: Bubble Sort y Timsort ---")
    ejercicio_t3()

    print("\n==========================================")
    print("     PRUEBA DE EJERCICIOS (Propuestos)    ")
    print("==========================================")

    print("\n--- P1: Contar apariciones ---")
    ejercicio_p1()

    print("\n--- P2: Invertir lista ---")
    ejercicio_p2()

    print("\n--- P3: Números únicos ---")
    ejercicio_p3()

    print("\n--- P4: Segundo mayor ---")
    ejercicio_p4()

    print("\n--- P5: Fusionar listas ordenadas ---")
    ejercicio_p5()