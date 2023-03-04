# Module imports
from jutl.pipelining import InstructionPipeline
from jutl.timers import Timer

# External class visibility
__all__ = ['Latency']


class Latency():
    """
    Class which calculates the latency
    of a single function or method call.
    """
    def __init__(self, func: function):
        "Initialization method."
        self.func: function = func
        self.pipeline: InstructionPipeline = InstructionPipeline(name="Latency")
        self.timer: Timer = Timer(name="Latency")
    
    def __call__(self, data: object = None) -> None:
        self.timer.start()
        result = self.func(data)
        self.timer.stop()
        return result
