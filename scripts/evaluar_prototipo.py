from nlp_pipeline import cargar_nlp_evaluacion
import time

# Load pipeline and data
nlp, all_labels, df = cargar_nlp_evaluacion()

TP = FP = FN = 0
tiempos = []

# Evaluate all records
for _, row in df.iterrows():
    texto = f"{row['motivo_consulta']}. {row['diagnostico_presuntivo']}. {row['observaciones']}. {row['tratamiento_indicado']}."
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

# Calculate metrics
precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
tiempo_promedio = sum(tiempos) / len(tiempos)

# Show results
print("\nResultados de evaluacion del prototipo:")
print(f"Precision: {precision:.2f}")
print(f"Exhaustividad: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
print(f"Tiempo promedio por registro: {tiempo_promedio:.2f} segundos")
