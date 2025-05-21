# Sistema de Anotaciones Automáticas en Registros Electrónicos de Salud (Tesis)

Este repositorio contiene el código fuente y los datos sintéticos utilizados en el trabajo de graduación titulado:

**“Diseño e Implementación de un Sistema para Anotaciones Automáticas en Registros Electrónicos de Salud mediante NLP y ML”**  
Autor: **Alberto Gabriel Reyes Ning**  
Universidad de San Carlos de Guatemala – Facultad de Ingeniería  
Mayo, 2025

---

## 🧠 Descripción del Proyecto

Este proyecto implementa un sistema prototipo que utiliza técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **Aprendizaje Automático (ML)** para generar anotaciones automáticas sobre texto clínico no estructurado.

Se simula el entorno de un registro electrónico de salud mediante un conjunto de datos sintéticos, permitiendo evaluar el comportamiento del sistema en tareas como extracción de síntomas, diagnósticos, tratamientos y procedimientos.

---

## ⚙️ Componentes del Sistema

- **`generar_csv.py`**: Crea un conjunto de 100 registros clínicos sintéticos.
- **`nlp_pipeline.py`**: Define el modelo de procesamiento y los patrones de anotación clínica.
- **`evaluar_prototipo.py`**: Ejecuta la evaluación cuantitativa del sistema (precisión, recall, F1).
- **`realizar_prueba.py`**: Visualiza anotaciones generadas con `displaCy`.
- **`spacy_load.py`**: Descarga el modelo `es_dep_news_trf` necesario para spaCy.

---

## 📂 Estructura del Proyecto

```
/prototipo-nlp-clinico/
│
├── scripts/                                     # Código fuente del sistema
│   ├── data/                                    # Datos clínicos sintéticos
│   │   └── notas_clinicas_sinteticas.csv        # Archivo CSV con 100 registros generados
│   ├── outputs/                                 # Archivos de salida generados por el sistema
│   │   └── resultado_prueba.json                # Entidades anotadas para un registro de prueba individual
│   │   └── resultado_evaluacion.json            # Resultado en lote de entidades anotadas en los 100 registros sintéticos
│   ├── env.bat                                  # Script para inicializar entorno virtual en Windows
│   ├── generar_csv.py                           # Generación de registros clínicos sintéticos
│   ├── nlp_pipeline.py                          # Carga del modelo BETO y patrones de anotación
│   ├── evaluar_prototipo.py                     # Evaluación de precisión, recall y F1
│   ├── spacy_load.py                            # Descarga e instalación del modelo es_dep_news_trf
│   └── realizar_prueba.py                       # Visualización interactiva de anotaciones con displaCy
└── README.md                                    # Documentación técnica del proyecto
```


---

## 📊 Resultados Clave

- Precisión: 1.00  
- Exhaustividad: 0.97  
- F1-score: 0.98  
- Tiempo promedio de anotación: 0.05 s por registro  

*(ver sección 4.3.3 del documento de tesis para el análisis completo)*

---

## ⚠️ Aviso Ético y Legal

> Este proyecto **no utiliza datos reales de pacientes**. Todos los registros fueron generados sintéticamente con fines académicos.  
>  
> El sistema no está diseñado para su uso en producción médica.  
>  
> Se prohíbe el uso del contenido de este repositorio con fines clínicos reales sin validación profesional adicional.

---

## 📄 Licencia

Este repositorio se publica bajo la licencia **MIT**. Puedes reutilizar el código con fines académicos o de investigación siempre que se otorgue el debido crédito.

---

## 📫 Contacto

Para preguntas o colaboración académica:

**Alberto Gabriel Reyes Ning**  
📧 agrn96p@gmail.com

