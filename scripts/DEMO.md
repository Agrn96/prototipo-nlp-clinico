# Demo interactiva

Desde la carpeta `scripts`, con el entorno activado:

```powershell
python realizar_prueba.py
```

Espera el mensaje `Demo lista` y abre http://localhost:5000. Si la versión
anterior está abierta, detenla con Ctrl+C antes de iniciar la nueva.

1. Selecciona **Ejemplo completo** y pulsa **Anotar texto** para mostrar las cuatro categorías.
2. Edita la nota y vuelve a anotarla; la tabla y los colores corresponden al texto enviado.
3. Usa **Paráfrasis** para explicar las limitaciones del vocabulario.
4. Usa **Negación** para mostrar que una coincidencia no confirma una condición.
5. Descarga el JSON con texto, entidades, posiciones y tiempo de procesamiento.

El modelo se carga una vez al iniciar el servidor. Cada análisis actualiza
`outputs/resultado_prueba.json`. El servidor usa únicamente la interfaz local
127.0.0.1 y no necesita dependencias web adicionales. Ctrl+C lo detiene.

Las etiquetas clínicas proceden del EntityRuler y del vocabulario del CSV.
Esta demostración no entrena un modelo ni corrige la evaluación existente.
