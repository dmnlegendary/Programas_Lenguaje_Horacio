# Utiliza el diccionario de vocabulario y funciones ya definidos
# Vocabulario en español e inglés con sus correspondientes etiquetas
vocabulario = {
    'espanol': {
        'palabras': ["El", "La", "Casa", "Roja", "Sol", "Y", "Arcoiris", "Son", "Luz", "Flor", "Grande", "Amarillo"],
        'etiquetas': ["Ar", "Ar", "S", "Ad", "S", "C", "S", "V", "V", "S", "Ad", "Ad"]
    },
    'ingles': {
        'palabras': ["The", "The", "House", "Red", "Sun", "And", "Rainbow", "Are", "Light", "Flower", "Big", "Yellow"],
        'etiquetas': ["Ar", "Ar", "S", "Ad", "S", "C", "S", "V", "V", "S", "Ad", "Ad"]
    }
}

# Función para encontrar la etiqueta de una palabra dada
def buscar_etiqueta(palabra, idioma):
    if palabra in vocabulario[idioma]['palabras']:
        indice = vocabulario[idioma]['palabras'].index(palabra)
        return vocabulario[idioma]['etiquetas'][indice]
    return None

# Función para cargar reglas desde un archivo
def cargar_reglas(nombre_archivo="reglas.txt"):
    reglas = {}
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.replace('-->', '->').strip()
            if "->" in linea:
                clave, valor = linea.split(" -> ")
                reglas[clave.strip()] = valor.strip().split()
    return reglas

# Función para obtener la traducción y etiqueta en inglés de una palabra en español
def obtener_traduccion_y_etiqueta(palabra):
    if palabra in vocabulario['espanol']['palabras']:
        indice = vocabulario['espanol']['palabras'].index(palabra)
        palabra_ingles = vocabulario['ingles']['palabras'][indice]
        etiqueta_ingles = vocabulario['ingles']['etiquetas'][indice]
        return palabra_ingles, etiqueta_ingles
    return None, None

# Función para aplicar las reglas para reordenar las palabras en inglés basado en sus etiquetas
def aplicar_reglas(etiquetas, palabras, reglas):
    secuencia_etiquetas = " ".join(etiquetas)
    if secuencia_etiquetas in reglas:
        nuevo_orden = reglas[secuencia_etiquetas]
        palabras_reordenadas = []
        for etiqueta in nuevo_orden:
            for i, etiqueta_actual in enumerate(etiquetas):
                if etiqueta_actual == etiqueta and palabras[i] not in palabras_reordenadas:
                    palabras_reordenadas.append(palabras[i])
                    break
        return palabras_reordenadas
    return palabras

# Cargar reglas desde el archivo
reglas = cargar_reglas()

# Obtener la oración en español del usuario
oracion_espanol = input("Introduce una oración en español: ")
palabras_espanol = oracion_espanol.split()

# Obtener las etiquetas para las palabras en español
etiquetas_espanol = [buscar_etiqueta(palabra, 'espanol') for palabra in palabras_espanol]

# Verificar si todas las palabras tienen etiquetas
if None in etiquetas_espanol:
    print("Algunas palabras no tienen etiqueta. Revisa tu oración.")
else:
    # Obtener la traducción al inglés y las etiquetas
    traducciones_ingles = []
    etiquetas_ingles = []
    for palabra in palabras_espanol:
        traduccion, etiqueta = obtener_traduccion_y_etiqueta(palabra)
        if traduccion and etiqueta:
            traducciones_ingles.append(traduccion)
            etiquetas_ingles.append(etiqueta)

    # Aplicar reglas para reordenar las palabras en inglés
    palabras_ingles_reordenadas = aplicar_reglas(etiquetas_ingles, traducciones_ingles, reglas)

    # Imprimir los resultados
    print(f"Oración en español: {' '.join(palabras_espanol)}")
    print(f"Etiquetas en español: {' '.join(etiquetas_espanol)}")
    print(f"Traducción al inglés: {' '.join(traducciones_ingles)}")
    print(f"Etiquetas en inglés: {' '.join(etiquetas_ingles)}")
    print(f"Oración reordenada según las reglas: {' '.join(palabras_ingles_reordenadas)}")
