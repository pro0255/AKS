from src.config import directory
import os
from enum import Enum

def load_data(path):
    print(f'Loading {path}')
    content = ''
    with open(path, 'r', encoding='windows-1252', errors='replace') as f:
        content = f.read()
    return content


def get_all_paths(directory = directory):
    all_directories = []
    for dir in os.listdir(directory):
        for nested_dir in os.listdir(os.path.sep.join([directory, dir])):
            all_directories.append(os.path.sep.join([directory, dir, nested_dir]))
    return all_directories




class DataSets(Enum):
    dna = "dna"
    english = "english"
    proteins = "proteins"
    sources = "sources"


def get_dataset(dataset_type):
    paths = get_all_paths()

    if DataSets.dna == dataset_type:
        return load_data(paths[0])
    if DataSets.english == dataset_type:
        return load_data(paths[1])
    if DataSets.proteins == dataset_type:
        return load_data(paths[2])
    if DataSets.sources == dataset_type:
        return load_data(paths[3])





