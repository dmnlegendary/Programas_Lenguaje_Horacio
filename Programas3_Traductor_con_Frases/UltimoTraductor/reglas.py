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

# Función para procesar oraciones y extraer reglas
def procesar_oraciones(oracion_es, oracion_en):
    palabras_es = oracion_es.split()
    palabras_en = oracion_en.split()
    etiquetas_es = [buscar_etiqueta(palabra, 'espanol') for palabra in palabras_es]
    etiquetas_en = [buscar_etiqueta(palabra, 'ingles') for palabra in palabras_en]
    
    if None in etiquetas_es or None in etiquetas_en:
        print("Algunas palabras no tienen etiqueta. Revisa las oraciones.")
    else:
        secuencia_es = " ".join(etiquetas_es)
        secuencia_en = " ".join(etiquetas_en)
        regla = f"{secuencia_es} --> {secuencia_en}"
        print("Regla extraída:", regla)
        guardar_regla(regla)

# Función para guardar las reglas en un archivo
def guardar_regla(regla):
    with open("reglas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(regla + "\n")

# Entrada de oraciones por parte del usuario
oracion_es = input("Introduce una oración en español: ")
oracion_en = input("Introduce la traducción al inglés: ")

# Procesamiento de las oraciones
procesar_oraciones(oracion_es, oracion_en)
