import spacy
from spacy.pipeline import EntityRuler
import pandas as pd

def cargar_nlp():
    # Load model
    nlp = spacy.load("es_dep_news_trf")
    ruler = nlp.add_pipe("entity_ruler", last=True)

    # Load CSV file
    df = pd.read_csv("data/notas_clinicas_sinteticas.csv")

    # Extract unique terms from relevant columns
    entity_dict = {
        "SINTOMA": df["motivo_consulta"].dropna().unique().tolist(),
        "DIAGNOSTICO": df["diagnostico_presuntivo"].dropna().unique().tolist(),
        "TRATAMIENTO": df["tratamiento_indicado"].dropna().unique().tolist(),
        "PROCEDIMIENTO": df["observaciones"].dropna().unique().tolist(),
    }

    # Build lowercased token patterns
    patterns = []
    for label, phrases in entity_dict.items():
        for phrase in phrases:
            pattern = [{"LOWER": token.lower()} for token in phrase.split()]
            patterns.append({"label": label, "pattern": pattern})

    # Add patterns to the ruler
    ruler.add_patterns(patterns)
    print(f"Patrones cargados: {len(patterns)} entidades")
    return nlp


def cargar_nlp_evaluacion():
    # Load model
    nlp = spacy.load("es_dep_news_trf")
    ruler = nlp.add_pipe("entity_ruler", last=True)

    # Load CSV file
    df = pd.read_csv("data/notas_clinicas_sinteticas.csv")

    # Extract unique terms from relevant columns
    entity_dict = {
        "SINTOMA": df["motivo_consulta"].dropna().unique().tolist(),
        "DIAGNOSTICO": df["diagnostico_presuntivo"].dropna().unique().tolist(),
        "TRATAMIENTO": df["tratamiento_indicado"].dropna().unique().tolist(),
        "PROCEDIMIENTO": df["observaciones"].dropna().unique().tolist(),
    }

    # Build lowercased token patterns
    patterns = []
    for label, phrases in entity_dict.items():
        for phrase in phrases:
            pattern = [{"LOWER": token.lower()} for token in phrase.split()]
            patterns.append({"label": label, "pattern": pattern})

    # Add patterns to the ruler
    ruler.add_patterns(patterns)
    print(f"Patrones cargados: {len(patterns)} entidades")
    all_labels = list(entity_dict.keys())
    return nlp, all_labels, df

