# Module imports

# External class visibility
__all__ = ['DataPipeline']


class DataPipeline(object):
    """
    Class which implements a data
    pipeline by connecting the data
    flow between passed functions.
    """
    def __init__(self, name: str = None):
        "Initialization method."
        self.name: str = name
        self.functions: list[object] = []

    def add_function(self, function: object):
        "Adds a function to the pipeline."
        self.functions.append(function)

    def run(self, *args, **kwargs):
        "Runs the pipeline."
        for function in self.functions:
            function(*args, **kwargs)