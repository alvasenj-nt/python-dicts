### **Rúbrica de Evaluación - Práctica de Procesamiento de Datos (Sobre 10 Puntos)**

**Nota Importante:** La entrega debe realizarse obligatoriamente a través de un enlace a un repositorio de GitHub. De no ser así, la práctica se considerará **no entregada** y la calificación será de 0, independientemente de los siguientes criterios.

---

#### **Criterio 1: Funcionalidad del Programa (4 Puntos)**

*   **(1 pto) Lectura y Validación:** Lee y valida correctamente los ficheros `csv` y `txt`, descartando filas con un número de campos incorrecto.
*   **(1 pto) Limpieza y Agrupación:** Normaliza los nombres de alumnos, ignora notas no válidas y agrupa todas las notas de cada alumno de forma correcta.
*   **(1 pto) Cálculos:** Calcula el promedio exacto para cada alumno y cruza los datos de becas eficientemente.
*   **(1 pto) Visualización:** Genera correctamente tanto la tabla en consola como la gráfica `notes_graph.png` con todos los requisitos visuales (colores, línea de aprobado, etc.).

---

#### **Criterio 2: Calidad y Estructura del Código (3 Puntos)**

*   **(1 pto) Modularidad:** El código está bien organizado en funciones con responsabilidades claras y se ejecuta desde un bloque `if __name__ == "__main__":`.
*   **(1 pto) Eficiencia y Estructuras de Datos:** Utiliza diccionarios para agrupar notas y para la búsqueda de becas, evitando bucles anidados e ineficientes.
*   **(1 pto) Claridad y Estilo:** El código es legible, con nombres de variables descriptivos y un formato consistente. Se valora positivamente el uso de `docstrings` y `type hints`.

---

#### **Criterio 3: Estructura y Entrega del Proyecto (3 Puntos)**

*   **(1 pto) Gestión del Entorno:** El `README.md` explica cómo crear el entorno virtual y el fichero `requirements.txt` existe y es correcto.
*   **(1 pto) Documentación (`README.md`):** El `README.md` es claro, completo e incluye una descripción del proyecto, las instrucciones de instalación/ejecución y una breve explicación del código.
*   **(1 pto) Jerarquía de Ficheros:** La estructura de ficheros del proyecto es limpia y contiene todos los artefactos necesarios (`.gitignore`, `main.py`, `README.md`, etc.).
