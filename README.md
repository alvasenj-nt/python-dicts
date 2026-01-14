# Procesador de Calificaciones de Alumnos

Este proyecto es una solución para el ejercicio de procesamiento de datos de alumnos. El script `main.py` lee las calificaciones y el estado de las becas desde archivos de texto (`.csv` y `.txt`), limpia y procesa los datos, y finalmente presenta un informe consolidado por la consola y una gráfica de barras con los resultados.

## Características

- **Limpieza de Datos:** Normaliza los nombres de los alumnos (eliminando espacios y unificando capitalización) e ignora las notas no válidas.
- **Validación de Ficheros:** Procesa únicamente las filas de los ficheros CSV que tienen el mismo número de columnas que la cabecera, garantizando la integridad de los datos.
- **Cálculo de Promedios:** Agrupa todas las notas de cada alumno y calcula su promedio final de forma precisa.
- **Cruce de Datos Eficiente:** Combina los datos de calificaciones con la información sobre becas usando una búsqueda rápida en un diccionario.
- **Visualización:** Muestra los resultados en una tabla en la consola y genera un gráfico de barras (`notes_graph.png`) coloreado según si el alumno ha aprobado o suspendido.

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto. Se asume que tienes Python 3 y Git instalados.

1.  **Clonar el Repositorio**

    Primero, clona este repositorio en tu máquina local desde GitHub.

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO_CLONADO>
    ```
    *(Nota: Deberás reemplazar la URL y el nombre del directorio con los valores correctos).*

2.  **Crear el Entorno Virtual**

    Un **entorno virtual** (`venv`) es un directorio aislado que contiene una instalación de Python y unas dependencias específicas para un proyecto. Esto evita conflictos entre las librerías de diferentes proyectos.

    Una vez dentro del directorio del proyecto, crea el entorno virtual:
    ```bash
    python -m venv practica_diccionarios
    ```

3.  **Activar el Entorno Virtual**

    La activación varía según el sistema operativo y la terminal que uses:

    - **En macOS y Linux (Bash/Zsh):**
      ```bash
      source practica_diccionarios/bin/activate
      ```
    - **En Windows (Command Prompt - CMD):**
      ```bash
      practica_diccionarios\Scripts\activate.bat
      ```
    - **En Windows (PowerShell, terminal por defecto en VS Code o ):**
      ```powershell
      .\practica_diccionarios\Scripts\Activate.ps1
      ```
      > **Solución de problemas en PowerShell:** Si al ejecutar este comando recibes un error sobre que la ejecución de scripts está deshabilitada, abre una nueva terminal de PowerShell y ejecuta lo siguiente (solo necesitas hacerlo una vez en tu equipo):
      > ```powershell
      > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
      > ```
      > Confirma la acción con `S` o `Y` y vuelve a intentar la activación.

4.  **Instalar Dependencias**

    Con el entorno activado, instala las librerías necesarias.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Ejecutar el Script**

    Finalmente, ejecuta el script principal:

    ```bash
    python main.py
    ```

## Salida del Programa

Al ejecutar el script, obtendrás dos salidas:

1.  Una **tabla en la consola** con el nombre, nota promedio, estado (APROBADO/SUSPENSO) y beca (SI/NO) de cada alumno.
2.  Un **nuevo fichero de imagen** llamado `notes_graph.png` en el directorio, con la gráfica de barras de las notas.

## Breve Explicación del Código (`main.py`)

El script está organizado en varias funciones para una mayor legibilidad y mantenibilidad:

- `read_csv`: Lee y valida el fichero `ej30notasdaw.csv`.
- `normalize_data`: Agrupa todas las notas de un mismo alumno en un diccionario (`{'Nombre': [lista_de_notas]}`).
- `calculate_notes`: A partir del diccionario anterior, calcula la nota media y el estado de cada alumno.
- `read_txt` y `clean_data_becas`: Leen y procesan el fichero `ej30becas.txt` en un diccionario para una búsqueda de becas eficiente.
- `cross_data`: Cruza los datos de notas y becas de forma rápida usando el diccionario de becas.
- `data_str`: Imprime la tabla final en la consola.
- `data_graph`: Genera y guarda la gráfica de barras.
