def fibonacci_recursiva(n): #funcion fiboancci recursiva
    if n < 0:
        raise ValueError("Entrada inválida: el Fibonacci no acepta negativos")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursiva(n-1) + fibonacci_recursiva(n-2)
def fibonacci_iterativa(n): #funcion fiboancci iteraticva
    if n < 0:
        raise ValueError("Entrada inválida: el Fibonacci no acepta negativos")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1  # inicializamos los primeros dos valores de fibonacci
    for _ in range(2, n + 1):
        a, b = b, a + b  # actualizamos los valores iterativamente
    return b

def ejecucion_programa(): #implento la ejecución del programa
    while True:
        try:
            numero = int(input("Ingrese un numero para calcular Fibonacci: "))
            resultado1 = fibonacci_recursiva(numero)
            print(f"el resultdo es {resultado1}")
        except ValueError as e: # manejo de caso especial numero negativo
           print(f"{e}")
        except KeyboardInterrupt: # finalizar programa
            print("\nPrograma finalizado.")
            break
if __name__ == "__main__":
    ejecucion_programa()