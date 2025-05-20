from nlp_pipeline import cargar_nlp
from spacy import displacy
import json
import os

# Cargar modelo NLP
nlp = cargar_nlp()

# Texto de prueba
texto = (
    "Paciente con fiebre persistente, dificultad respiratoria, y se solicita hemograma "
    "y ultrasonido abdominal y solicita TAC. Diagnóstico: neumonía bacteriana. "
    "Tratamiento: oxigenoterapia."
)

# Procesamiento
doc = nlp(texto)

# Extraer entidades a JSON
entidades = [
    {"texto": ent.text, "etiqueta": ent.label_}
    for ent in doc.ents
]

# Crear carpeta de salida si no existe
os.makedirs("outputs", exist_ok=True)

# Guardar salida en archivo JSON
with open("outputs/resultado_prueba.json", "w", encoding="utf-8") as f:
    json.dump(entidades, f, indent=4, ensure_ascii=False)

print("Archivo generado: outputs/resultado_prueba.json")

# Visualización interactiva (bloquea la ejecución hasta que se cierre)
displacy.serve(doc, style="ent")
