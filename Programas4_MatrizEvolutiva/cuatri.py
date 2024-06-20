import numpy as np
import random
from collections import Counter

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def calcular_estadisticas(texto):
    palabras = texto.split()
    total_palabras = len(palabras)
    palabras_unicas = len(set(palabras))
    frecuencia_palabras = Counter(palabras)
    palabras_mas_frecuentes = frecuencia_palabras.most_common(10)
    return total_palabras, palabras_unicas, palabras_mas_frecuentes

def construir_matriz_transicion(texto):
    palabras = texto.split()
    if len(palabras) < 4:
        raise ValueError("El texto debe contener al menos 3 palabras.")
    
    frases = [' '.join(palabras[i:i+3]) for i in range(len(palabras) - 2)]
    frases_unicas = sorted(list(set(frases)))
    indices = {frase: i for i, frase in enumerate(frases_unicas)}
    tamaño = len(frases_unicas)
    
    matriz = np.zeros((tamaño, tamaño))
    
    for i in range(len(frases) - 1):
        actual = indices[frases[i]]
        siguiente = indices[frases[i + 1]]
        matriz[actual][siguiente] += 1
    
    # Normalizar la matriz, manejando filas con suma cero y ajustando pequeñas diferencias numéricas
    for i in range(tamaño):
        suma = matriz[i].sum()
        if suma != 0:
            matriz[i] /= suma
        else:
            matriz[i] = np.zeros(tamaño)
    
    # Asegurar que todas las filas sumen exactamente 1
    for i in range(tamaño):
        if matriz[i].sum() != 0:
            matriz[i] /= matriz[i].sum()
    
    return frases_unicas, matriz

def generar_texto_frases(frases_unicas, matriz, longitud_texto):
    frase_inicial = random.choice(frases_unicas)
    palabras = frase_inicial.split()
    actual = frases_unicas.index(frase_inicial)
    
    for _ in range(longitud_texto - 3):
        if matriz[actual].sum() == 0:
            actual = random.choice(range(len(frases_unicas)))
        else:
            actual = np.random.choice(range(len(frases_unicas)), p=matriz[actual])
        siguiente_frase = frases_unicas[actual]
        palabras.extend(siguiente_frase.split()[2:3])  # Solo añadir la última palabra de la frase siguiente
    
    return ' '.join(palabras)

def imprimir_matriz(frases_unicas, matriz):
    max_len = max(len(frase) for frase in frases_unicas)
    fmt = f"{{:>{max_len}}}"  # Formato para alinear las frases
    with open('matriz4_frec.txt', 'w', encoding='utf-8') as archivo:
        # Encabezado de las columnas
        archivo.write(f"{' ':{max_len}}")
        for frase in frases_unicas:
            archivo.write(fmt.format(frase) + " ")
        archivo.write('\n')
    
        # Filas de la matriz
        for i, row in enumerate(matriz):
            archivo.write(fmt.format(frases_unicas[i]) + " ")  # Encabezado de la fila
            for prob in row:
                archivo.write(f"{prob:>{max_len}.4f} ")  # Probabilidad con 4 decimales
            archivo.write('\n')

nombre_archivo = 'texto.txt'  
texto = leer_archivo(nombre_archivo)

# Calcular estadísticas
total_palabras, palabras_unicas, palabras_mas_frecuentes = calcular_estadisticas(texto)
print(f"Total de palabras: {total_palabras}")
print(f"Palabras únicas: {palabras_unicas}")
print("Palabras más frecuentes:")
for palabra, frecuencia in palabras_mas_frecuentes:
    print(f"{palabra}: {frecuencia}")

frases_unicas, matriz = construir_matriz_transicion(texto)
texto_generado_frases = generar_texto_frases(frases_unicas, matriz, 100)  

print(f'Texto generado por frases de tres palabras: \n {texto_generado_frases} \n \n')
imprimir_matriz(frases_unicas, matriz)
print(f"Matriz de transición impresa en 'matriz4_frases.txt'.")
