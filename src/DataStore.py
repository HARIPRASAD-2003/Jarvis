# data_store.py
import json

class DataStore:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_data()

    def remove(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()
