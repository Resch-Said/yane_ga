from abc import ABC, abstractmethod


class CustomGene(ABC):
    @abstractmethod
    def mutate(self):
        pass
