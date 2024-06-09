import re

def replace_words(text, corrections):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in corrections.keys()) + r')\b')
    result = pattern.sub(lambda x: corrections[x.group()], text)
    return result

# Diccionario de correcciones
corrections = {
    "karro": "carro",
    "komer": "comer",
    "kuando": "cuando"
    # Añade más palabras según sea necesario
}

# Ejemplo de uso
text = "karo"
corrected_text = replace_words(text, corrections)
print("Texto original:", text)
print("Texto corregido:", corrected_text)
