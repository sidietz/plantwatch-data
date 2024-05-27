import os
import json

def get_files_from_folder(folder):
    onlyfiles = [folder + "/" + f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    onlyfiles.sort()
    files = [f for f in onlyfiles if os.stat(f).st_size > MIN_SIZE]
    return files

def get_plant(f):
    return f.split("/")[2].rsplit("_", 4)[0]

def get_mapper(file):
    mapper = {}
    with open(file, 'r') as myfile:
        tmp = myfile.read()
        mapper = json.loads(tmp)
    return mapper

BASE_DIR = "."
MIN_SIZE = 512

