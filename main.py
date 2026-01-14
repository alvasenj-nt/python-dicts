import csv
import matplotlib.pyplot as plt

def read_csv(file_path):
    """
    Reads a CSV file and returns its content as a list of dictionaries.
    Rows with inconsistent number of fields are skipped.
    Parameters:
        file_path (str): Path to the CSV file.
    Returns:
        list: List of dictionaries representing the CSV data.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        try:
            header_names = dict_reader.fieldnames
            num_header_fields = len(header_names)
        except TypeError:
            return []

        for row_list in dict_reader.reader:
            if len(row_list) == num_header_fields:
                dict_row = dict(zip(header_names, row_list))
                data.append(dict_row)
    return data

def normalize_csv_data(data: list) -> list:
    """
    Normalizes the CSV data by cleaning names and filtering valid notes.
    Parameters:
        data (list): List of dictionaries with raw CSV data.
    Returns:
        dict: Dictionary with cleaned names as keys and list of valid notes as values.
    """
    normalized_data = {}
    for row in data:
        try:
            float(row['Nota'].strip())
            normalized_data.setdefault(row['Nombre'].strip().title(), []).append(row['Nota'].strip())
        except ValueError:
            continue
    return normalized_data

def calculate_notes(normalized_data: dict) -> list:
    """
    Calculates average notes and determines pass/fail status.
    Parameters:
        normalized_data (dict): Dictionary with names and list of notes.
    Returns:
        list: List of dictionaries with average notes and status.
    """
    avg_data = []
    for name, notes in normalized_data.items():
        avg_notes = {}
        avg_notes["Nombre"] = name
        avg_notes["Nota"] = sum(float(note) for note in notes) / len(notes)
        avg_notes["Estado"] = "APROBADO" if avg_notes["Nota"] >= 5 else "SUSPENSO"
        avg_data.append(avg_notes)
    return avg_data

def read_txt(file_path):
    """Reads a TXT file and returns its content as a list of lines."""
    with open(file_path, mode='r', encoding='utf-8') as txtfile:
        data = [line.strip() for line in txtfile.readlines()]
        return data

def normalize_txt_data(data: list) -> list:
    """
    Normalizes the TXT data by cleaning names and scholarship status.
    Parameters:
        data (list): List of lines from the TXT file.
    Returns:
        dict: Dictionary with cleaned names as keys and scholarship status as values.
    """
    cleaned_data = {}
    for line in data:
        name, scolarship = line.split(':', 1)
        name_clean = name.strip().title()
        scolarship_clean = scolarship.strip().upper()
        cleaned_data[name_clean] = scolarship_clean
    return cleaned_data

def cross_data(avg_data: list, cleaned_data_becas: dict) -> None:
    """
    Cross-references average notes data with scholarship data.
    Parameters:
        avg_data (list): List of dictionaries with average notes and status.
        cleaned_data_becas (dict): Dictionary with scholarship status.
    Modifies avg_data in place to add scholarship status.
    """
    for row in avg_data:
        name = row['Nombre']
        row['Beca'] = cleaned_data_becas.get(name, 'NO')

def data_to_str(swapped_data: list) -> None:
    """
    Displays the final data in a formatted table.
    Parameters:
        swapped_data (list): List of dictionaries with final data.
    """
    print(f"{'ALUMNO':<12} {'|':<2} {'NOTA':<10} {'|':<2} {'ESTADO':<10} {'|':<2} {'BECA':<10}")
    print("-" * 45)
    for row in swapped_data:
        print(f"{row['Nombre']:<12} {'|':<2} {row['Nota']:<10} {'|':<2} {row['Estado']:<10} {'|':<2} {row['Beca']:<10}")

def data_to_graph(swapped_data: list) -> None:
    """
    Generates and saves a bar graph of the notes data.
    Parameters:
        swapped_data (list): List of dictionaries with final data.
    """
    names = [row['Nombre'] + ('(*)' if row['Beca'] != 'NO' else '') for row in swapped_data]
    notes = [row['Nota'] for row in swapped_data]
    colors = ['green' if row['Estado'] == 'APROBADO' else 'red' for row in swapped_data]
    plt.bar(names, notes, color=colors)
    plt.xlabel('Alumnos')
    plt.ylabel('Nota Promedio')
    plt.title('Calificaciones Finales y Estado de Beca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.axhline(y=5.0, color='blue', linestyle='--', label='Corte Aprobado')
    plt.savefig('notes_graph.png')

if __name__ == "__main__":
    data_notes = read_csv('ej30notasdaw.csv')
    normalized_data_notes = normalize_csv_data(data_notes)
    avg_data = calculate_notes(normalized_data_notes)
    data_becas = read_txt('ej30becas.txt')
    cleaned_data_becas = normalize_txt_data(data_becas)
    cross_data(avg_data, cleaned_data_becas)
    data_to_str(avg_data)
    data_to_graph(avg_data)