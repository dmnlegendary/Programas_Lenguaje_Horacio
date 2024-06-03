from textblob import TextBlob

def correct_text(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)

# Ejemplo de uso
text = "Este es un karro muy rapido."
corrected_text = correct_text(text)
print("Texto original:", text)
print("Texto corregido:", corrected_text)
