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
    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.name is None:
            if len(self.functions) < 1:
                return f"DataPipeline()"
            else:
                return f"DataPipeline({len(self.functions)})"
        else:
            if len(self.functions) >= 1:
                return f"DataPipeline({self.name}, {len(self.functions)})"
            else:
                return f"DataPipeline({self.name})"

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
