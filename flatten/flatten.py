def aplanar_lista(lista_anidada): # implementacion para aplanar lista
    lista_plana = []
    for elemento in lista_anidada:
        if isinstance(elemento, (list, tuple)):  # Maneja listas y tuplas
            lista_plana.extend(aplanar_lista(elemento))
        elif isinstance(elemento, dict):  # Maneja diccionarios
            lista_plana.extend(aplanar_lista(list(elemento.items())))
        else:
            lista_plana.append(elemento)
    return lista_plana

def ejecutar_programa(): # ejecucion de programa

    while True:
        try:
            entrada = input("Ingrese una lista anidada: ")
            lista = eval(entrada)  # convierte el string a lista/tupla/dict
            resultado = aplanar_lista(lista)
            print(f"Lista aplanada: {resultado}\n")
            
        except KeyboardInterrupt: # finalizar programa
            print("\nPrograma finalizado.")
            break
if __name__ == "__main__":
    ejecutar_programa()