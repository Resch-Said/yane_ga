import json


class Config:
    config_path = "../config.json"

    @classmethod
    def get(cls):
        with open(cls.config_path, "r") as f:
            config = json.load(f)
            return config

    @classmethod
    def get_gene_mutation_rate(cls):
        return cls.get()["gene"]["mutation_rate"]

    @classmethod
    def get_value_pool(cls):
        return cls.get()["gene"]["value_pool"]

    @classmethod
    def get_min_value(cls):
        return cls.get()["gene"]["min_value"]

    @classmethod
    def get_max_value(cls):
        return cls.get()["gene"]["max_value"]

    @classmethod
    def get_tournament_selection_k(cls):
        return cls.get()["population"]["tournament_size"]
