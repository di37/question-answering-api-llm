import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

DATA_PATH = os.getenv("DATA_PATH", "items/data")
INDEX_FILE_PATH = os.getenv("INDEX_FILE_PATH", "items/index_folder/index.json")