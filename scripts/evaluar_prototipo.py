from nlp_pipeline import cargar_nlp_evaluacion
import time
import json
import os

# Cargar pipeline y datos
nlp, all_labels, df = cargar_nlp_evaluacion()

TP = FP = FN = 0
tiempos = []
resultados = []

# Evaluar cada registro
for i, row in enumerate(df.itertuples(), start=1):
    texto = f"{row.motivo_consulta}. {row.diagnostico_presuntivo}. {row.observaciones}. {row.tratamiento_indicado}."
    start = time.time()
    doc = nlp(texto)
    tiempos.append(time.time() - start)

    expected = set(all_labels)
    predicted = set(ent.label_ for ent in doc.ents if ent.label_ in all_labels)

    for label in all_labels:
        if label in expected and label in predicted:
            TP += 1
        elif label in predicted and label not in expected:
            FP += 1
        elif label in expected and label not in predicted:
            FN += 1

    entidades = [
        {"texto": ent.text, "etiqueta": ent.label_}
        for ent in doc.ents if ent.label_ in all_labels
    ]

    resultados.append({
        "registro": i,
        "texto": texto,
        "entidades_detectadas": entidades
    })

# Calcular métricas
precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
tiempo_promedio = sum(tiempos) / len(tiempos)

# Mostrar resultados en consola
print("\nResultados de evaluación del prototipo:")
print(f"Precisión: {precision:.2f}")
print(f"Exhaustividad: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
print(f"Tiempo promedio por registro: {tiempo_promedio:.2f} segundos")

# Guardar anotaciones en archivo JSON
os.makedirs("outputs", exist_ok=True)
with open("outputs/resultados_evaluacion.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=4, ensure_ascii=False)

print("Archivo generado: outputs/resultados_evaluacion.json")
