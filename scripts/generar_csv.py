import pandas as pd
import random
from faker import Faker

fake = Faker('es_ES')
random.seed(42)

# Motivos de consulta representativos de situaciones clínicas frecuentes
motivos = [
    "Dolor abdominal agudo",         # común en emergencias
    "Fiebre persistente",            # síntoma inespecífico con muchas causas
    "Dolor torácico",                # posible evento cardíaco
    "Fatiga crónica",                # causa frecuente en medicina interna
    "Cefalea intensa",              # puede indicar desde migraña hasta hemorragia
    "Dificultad respiratoria"       # clave para enfermedades pulmonares/infecciosas
]

# Diagnósticos presuntivos variados en frecuencia y gravedad
diagnosticos = [
    "Apendicitis aguda",            # urgencia quirúrgica común
    "Neumonía bacteriana",          # infección respiratoria frecuente
    "Migraña crónica",              # condición neurológica común
    "Hipertensión esencial",        # enfermedad crónica prevalente
    "COVID-19 leve",                # vigente y con síntomas amplios
    "Gastritis"                     # muy común en consultas generales
]

# Tratamientos que simulan medidas médicas estándar
tratamientos = [
    "Reposo, líquidos y analgésicos",           # manejo conservador
    "Antibióticos y observación",              # típico de infecciones
    "Referido a cirugía",                      # casos urgentes
    "Monitoreo ambulatorio",                   # seguimiento no hospitalario
    "Oxigenoterapia",                          # soporte respiratorio
    "Cambio de dieta y omeprazol"              # tratamiento digestivo
]

# Antecedentes médicos realistas y diversos
antecedentes = [
    "Hipertensión controlada con losartán.",   # condición cardiovascular común
    "Diabetes mellitus tipo II.",              # crónica y frecuente
    "Sin antecedentes relevantes.",            # sano, control
    "Asma leve desde la infancia.",            # enfermedad respiratoria frecuente
    "Alergia a penicilina.",                   # importante para decisiones terapéuticas
    "Enfermedad renal crónica."                # relevante para dosificación
]

# Observaciones clínicas asociadas a la consulta
observaciones = [
    "Se solicita hemograma y ultrasonido abdominal",
    "Control en 48 horas",
    "Solicita TAC",
    "Se realiza espirometría",
    "Consulta con cardiología",
    "Monitorización de signos vitales"
]

# Generar registros
registros = []
for _ in range(100):
    registro = {
        "nombre_paciente": fake.name(),
        "edad": random.randint(18, 90),
        "sexo": random.choice(["Masculino", "Femenino"]),
        "fecha_consulta": fake.date_this_year(),
        "motivo_consulta": random.choice(motivos),
        "antecedentes": random.choice(antecedentes),
        "diagnostico_presuntivo": random.choice(diagnosticos),
        "tratamiento_indicado": random.choice(tratamientos),
        "observaciones": random.choice(observaciones)
    }
    registros.append(registro)

df = pd.DataFrame(registros)
df.to_csv("data/notas_clinicas_sinteticas.csv", index=False, encoding='utf-8')
print("Archivo generado: data/notas_clinicas_sinteticas.csv")
