class Palabra:
    def __init__(self, original, traduccion, etiquetas, contador):
        self.original = original
        self.traduccion = traduccion
        #etiquetas significado:
        # 1 --> Articulo
        # 2 --> Adjetivo
        # 3 --> Sustantivo
        # 4 --> Pronombre
        # 5 --> Verbo
        # 6 --> Adverbio
        # 7 --> Preposicion
        # 8 --> Conjugacion
        self.etiquetas = etiquetas
        self.contador = contador
    def __str__(self):
        return f"Original: {self.original}, Traducción: {self.traduccion}, Etiquetas: {self.etiquetas} Contador: {self.contador}"