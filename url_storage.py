import json
import os

URL_STORAGE_FILE = "url_storage.json"

# Завантаження URL зі сховища
def load_url_storage():
    if os.path.exists(URL_STORAGE_FILE):
        with open(URL_STORAGE_FILE, "r") as file:
            return json.load(file)
    return {}

# Збереження URL у сховище
def save_url_storage(data):
    with open(URL_STORAGE_FILE, "w") as file:
        json.dump(data, file)

# Ініціалізація URL сховища
url_storage = load_url_storage()