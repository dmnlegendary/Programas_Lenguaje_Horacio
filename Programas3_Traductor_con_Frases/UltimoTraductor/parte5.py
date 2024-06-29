palabrasEspanol = ["El", "La", "Casa", "Roja", "Sol", "Y", "Arcoiris", "Son", "Luz", "Flor", "Grande", "Amarillo"]
etiquetasEspanol = ["Ar", "Ar", "S", "Ad", "S", "C", "S", "V", "V", "S", "Ad", "Ad"]

palabrasIngles = ["The", "The", "House", "Red", "Sun", "And", "Rainbow", "Are", "Light", "Flower", "Big", "Yellow"]
etiquetasIngles = ["Ar", "Ar", "S", "Ad", "S", "C", "S", "V", "V", "S", "Ad", "Ad"]

with open("etiquetasEspanol.txt", "w", encoding="utf-8") as file:
    for index in range(len(palabrasEspanol)):
        file.write(f"{palabrasEspanol[index]} {etiquetasEspanol[index]}\n")

with open("etiquetasIngles.txt", "w", encoding="utf-8") as file:
    for index in range(len(palabrasIngles)):
        file.write(f"{palabrasIngles[index]} {etiquetasIngles[index]}\n")


