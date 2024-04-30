import json


class Config:
    config_path = '../config.json'

    @classmethod
    def get(cls):
        with open(cls.config_path, 'r') as f:
            config = json.load(f)
            return config

    @classmethod
    def get_gene_mutation_rate(cls):
        return cls.get()["gene"]["mutation_rate"]


