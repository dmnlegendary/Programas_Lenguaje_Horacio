from PIL import Image


def cargar_imagen(ruta):
    return Image.open(ruta).convert('L')


def xnor_difuso(imagen1, imagen2):
    diferencia = 0
    total_pixeles = imagen1.width * imagen1.height
    for x in range(imagen1.width):
        for y in range(imagen1.height):
            diferencia += abs(imagen1.getpixel((x, y)) - imagen2.getpixel((x, y)))
    similitud = (1 - diferencia / (255 * total_pixeles)) * 100
    return similitud


# Carga la imagen de prueba
prueba=int(input("Dame la imagen de prueba "))
imagen_prueba = cargar_imagen(f'C:\\Users\\LuisValle\\Desktop\\Lenguaje\\NUMEROS\\{prueba}.bmp')

# Cargar y comparar las imágenes de referencia
resultados_similitud = {}
for i in range(1,101):
    imagen_referencia = cargar_imagen(f'C:\\Users\\LuisValle\\Desktop\\Lenguaje\\NUMEROS\\{i}.bmp')
    if imagen_referencia.size != imagen_prueba.size:
        imagen_referencia = imagen_referencia.resize(imagen_prueba.size)
    similitud = xnor_difuso(imagen_prueba, imagen_referencia)
    resultados_similitud[i] = similitud

# Determinar cuál imagen de referencia es más similar
numero_mas_parecido = max(resultados_similitud, key=resultados_similitud.get)
similitud_max = resultados_similitud[numero_mas_parecido]

print(f"El número más parecido es: {numero_mas_parecido} con un {similitud_max:.2f}% de similitud.")
