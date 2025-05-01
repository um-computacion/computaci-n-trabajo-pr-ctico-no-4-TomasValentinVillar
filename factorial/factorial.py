def factorial_recursivo(n: int) -> int: #implemento la funcion factorial_recursivo para calcular el
                                        #facorial de un numero con una funcion recursiva
    if n < 0:
        raise ValueError("Entrada inválida: el factorial no acepta negativos")
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
def factorial_iterativo(n: int) -> int: #implemento la funcion factorial_recursivo para calcular el
                                        #facorial de un numero con una funcion recursiva
    if n < 0:
        raise ValueError("Entrada inválida: el factorial no acepta negativos")
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado

def ejecucion_programa(): #implento la ejecución del programa
    while True:
        try:
            numero = int(input("Ingrese un numero para calcular el factorial: "))
            resultado1 = factorial_iterativo(numero)
            print(f"el resultdo es {resultado1}")
        except ValueError as e: # manejo de caso especial numero negativo
           print(f"{e}")
        except KeyboardInterrupt: # finalizar programa
            print("\nPrograma finalizado.")
            break
if __name__ == "__main__":
    ejecucion_programa()