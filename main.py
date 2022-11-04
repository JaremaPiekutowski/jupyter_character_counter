import json
import os

# Filenames list
FILENAMES = os.listdir("data")


# Load files
def load_files_content(filenames: list) -> dict:
    files_content = dict()
    for filename in filenames:
        with open (f"data/{filename}", mode="r", encoding="utf-8") as f:
            files_content[f"{filename.split(sep='.')[0]}"] = json.loads(f.read())
    return files_content


# Get length of a file's content
def get_file_content_length(content: dict) -> int:
    return sum([len(element) for cell in content['cells'] for element in cell['source']])


# Create dictionary of lengths on the basis of the files provided, together with sum
def create_lengths_map(files_content: dict) -> dict:
    lengths = dict()
    for name, value in files_content.items():
        lengths[name] = get_file_content_length(value)
    # Add total length to the dictionary
    lengths["Suma"] = sum(lengths.values())
    return lengths


# Display lengths of all files and sum
def display_content_lengths(lengths: dict) -> None:
    if len(lengths) == 1:
        print ("Brak danych.")
    else:
        for key, value in lengths.items():
            print(f"{key}: {value} znaków")


if __name__ == "__main__":
    display_content_lengths(create_lengths_map(load_files_content(FILENAMES)))
