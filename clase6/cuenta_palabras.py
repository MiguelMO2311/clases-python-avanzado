from multiprocessing import Pool
from typing import Sequence
from pathlib import Path

ContadoresTexto = tuple[str, int, int]

def count_file(file_path: Path) -> ContadoresTexto:
    text = file_path.read_text()
    word_count = len(text.split())
    letter_count = sum(1 for char in text if char.isalpha())
    return file_path.name, word_count, letter_count

def count_files(file_paths: Sequence[Path]) -> list[ContadoresTexto]:
    with Pool() as pool:
        return pool.map(count_file, file_paths)

if __name__ == "__main__":
    current_directory = Path(".")
    txt_files = [file for file in current_directory.iterdir() 
                 if file.is_file() and file.suffix == ".txt"]
    results = count_files(txt_files)
    # A partir de aqui ya es interfaz para leerlo guay
    for filename, word_count, letter_count in results:
        print(f"{filename}: palabras={word_count}, letras={letter_count}")
    total_words = sum(result[1] for result in results)
    total_letters = sum(result[2] for result in results)
    print(f"Totales -> palabras={total_words}, letras={total_letters}")