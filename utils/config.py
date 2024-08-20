import json

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)