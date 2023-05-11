# Module imports
from jutl.formatting import apply
from time import time

# External class visibility
__all__ = ['Reporter']


class Reporter():
    """
    Class which acts as a timer to
    record loop times for comparison.
    """
    def __init__(self, name: str = None, declare_times: bool = False):
        "Initialization method."
        self.name: str = name
        self._start_time: float
        self._stop_time: float
        self.total_time: float = None
        self._loops: list[float] = []
        self.loop_times: list[float] = []
        self._declare_times = declare_times

    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.name is None:
            if self.total_time is None:
                return "Reporter()"
            else:
                return f"Reporter({round(self.total_time, 2)}s)"
        else:
            if self.total_time is None:
                return f"Reporter({self.name})"
            else:
                return f"Reporter({self.name}, {round(self.total_time, 2)}s)"
                
    def __call__(self, color: str = None):
        """
        Tells the interpreter what to
        do when an object of this
        class is called directly.
        """
        if self.loop_times:
            for n, time in enumerate(self.loop_times):
                if color:
                    print(apply(text=f"Loop {n+1}: {round(time, 2)}s", text_color=color))
                else:
                    print(f"Loop {n+1}: {round(time, 2)}s")
        else:
            print("There are no loop times.")

    def __len__(self) -> int:
        """
        Tells the interpreter what to
        consider this class' length.
        """
        return len(self._loops)
        
    def __iter__(self) -> iter:
        """
        Tells the interpreter what to
        iterate over thwn iterator methods
        are called on this class.
        """
        return iter(self.loop_times)
    
    def __eq__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles equal operators.
        """
        return self.total_time == other.total_time

    def __ne__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles not equal operators.
        """
        return self.total_time != other.total_time

    def __gt__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles greater than operators.
        """
        return self.total_time > other.total_time

    def __ge__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles greater or equal operators.
        """
        return self.total_time >= other.total_time

    def __lt__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles less than operators.
        """
        return self.total_time < other.total_time

    def __le__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles less than or equal operators.
        """
        return self.total_time <= other.total_time

    def __add__(self, other) -> float:
        """
        Tells the interpreter how to sum these objects.
        """
        return self.total_time + other.total_time

    def __sub__(self, other) -> float:
        """
        Tells the interpreter how to subtract these objects.
        """
        return self.total_time - other.total_time

    def __mul__(self, multiplier) -> float:
        """
        Tells the interpreter how to subtract these objects.
        """
        return self.total_time * multiplier

    def __truediv__(self, other) -> float:
        """
        Tells the interpreter how to subtract these objects.
        """
        return self.total_time / other.total_time
    

    def start(self, message: str = None, color : str = None):
        """
        Starts the reporter and
        optionall prints a message.
        """
        self._start_time = time()
        if message:
            print(apply(text=message, text_color=color) if color else print(message))

    
    def loop(self, loop_time: float = None, message: str = None, color: str = None):
        """
        Adds the current time to the loop
        time list, records the time since
        the start or time of the last recorded
        loop, and optionally prints a message.
        """
        if loop_time:
            self._loops.append(loop_time)
        else:
            self._loops.append(time())
        if not self.loop_times:
            self.loop_times.append(self._calculate_time(self._start_time, self._loops[-1]))
        else:
            self.loop_times.append(self._calculate_time(self._loops[-2], self._loops[-1]))
        if message:
            print(apply(text=message, text_color=color) if color else print(message))
    
    def stop(self, message: str = None, color: str = None):
        """
        Stops the reporter, calculates
        the total time passed, and
        optionally prints a message.
        """
        self._stop_time = time()
        self.total_time = self._calculate_time(self._start_time, self._stop_time)
        self.loop(self._stop_time) # add final loop time and calculate loop difference
        if message:
            print(apply(text=message, text_color=color) if color else print(text=message))


    def _calculate_time(self, time1: float, time2: float) -> float:
        """
        Returns the difference in time where t2>t1.
        """
        return time2 - time1
    

    def reset(self, message: str = None, color: str = None):
        """
        Resets all reporter attributes
        and optionally prints a message.
        """
        self._start_time = None
        self._stop_time = None
        self.total_time = None
        self._loops.clear()
        self.loop_times.clear()
        if message:
            print(apply(text=message, text_color=color) if color else print(text=message))
