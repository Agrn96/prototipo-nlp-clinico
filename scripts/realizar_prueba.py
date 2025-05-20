from nlp_pipeline import cargar_nlp
from spacy import displacy

nlp = cargar_nlp()
doc = nlp("Paciente con fiebre persistente, dificultad respiratoria, y se solicita hemograma y ultrasonido abdominal y solicita TAC. Diagnóstico: neumonía bacteriana. Tratamiento: oxigenoterapia.")
displacy.serve(doc, style="ent")
