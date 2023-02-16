# Module imports

# External class visibility
__all__ = ['InstructionPipeline']


class InstructionPipeline():
    """
    Class which implements an instruction
    pipeline which by connecting the data
    flow between passed functions.
    """
    def __init__(self, *functions: object, name: str = None):
        "Initialization method."
        self.name: str = name
        self.functions: list[object] = list(functions)

    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.name is None:
            if len(self.functions) < 1:
                return f"InstructionPipeline()"
            else:
                return f"InstructionPipeline({len(self.functions)})"
        else:
            if len(self.functions) >= 1:
                return f"InstructionPipeline({self.name}, {len(self.functions)})"
            else:
                return f"InstructionPipeline({self.name})"
    
    def __call__(self, data: None) -> None:
        """
        Executes the pipeline
        with passed data.
        """
        if len(self.functions) < 1:
            return data
        else:
            match type(data).__name__:
                case "int" | "float":
                    for function in self.functions:
                        data = function(data)
                case other:
                    print(f"Data type ({other}) is not supported.")
            return data
    
    def __len__(self) -> int:
        """
        Tells the interpreter what to
        consider this class' length.
        """
        return len(self.functions)
    
    def __iter__(self) -> object:
        """
        Tells the interpreter what to
        iterate over when iterator methods
        are called on this class.
        """
        return iter(self.functions)


    def add(self, *functions: object):
        """
        Adds a function to the pipeline.
        """
        for function in functions:
            self.functions.append(function)

    
    def list(self) -> None:
        """
        Lists all functions in the pipeline.
        """
        print(function.__name__ for function in self.functions)

    
    def remove(self, *functions: object):
        """
        Removes a function from the pipeline.
        """
        for function in functions:
            if function in self.functions:
                self.functions.remove(function)
            else:
                continue

    
    def clear(self):
        """
        Removes all functions from the pipeline.
        """
        self.functions.clear()
