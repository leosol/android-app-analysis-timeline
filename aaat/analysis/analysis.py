from abc import abstractmethod


class Analysis:
    def __init__(self):
        pass

    @abstractmethod
    def get_analyzers(self):
        raise NotImplementedError()

    @abstractmethod
    def process(self, file):
        raise NotImplementedError()
