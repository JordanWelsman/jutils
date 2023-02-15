# Module imports
from jutl.pipelining.instructionpipeline import InstructionPipeline

# External class visibility
__all__ = ['DataPipeline']


class DataPipeline(InstructionPipeline):
    """
    Class which extends the instruction
    pipeline and supports passing
    multiple instances of data.
    """
    def __call__(self, *data):
        """
        Executes the pipeline
        with passed data.
        """
        results: list = []
        for datum in data:
            match type(datum).__name__:
                case "int" | "float":
                    for function in self.functions:
                        datum = function(datum)
                    results.append(datum)
                case other:
                    print(f"Data type ({other}) is not supported.")
        return results
