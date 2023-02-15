# Module imports
from time import time, sleep

# External class visibility
__all__ = ['Timer']


class Timer():
    """
    Class which acts as a timer
    with time methods.
    """
    def __init__(self, name: str = None):
        "Initialization method."
        self.name: str = name
        self._start_time: float
        self._pause_time: float = None
        self._paused_time: float = None
        self._stop_time: float
        self.total_time: float = None

    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.name is None:
            if self.total_time is None:
                return "Timer()"
            else:
                return f"Timer({round(self.total_time, 2)}s)"
        else:
            if self.total_time is None:
                return f"Timer({self.name})"
            else:
                return f"Timer({self.name}, {round(self.total_time, 2)}s)"
    
    def __call__(self):
        """
        Tells the interpreter what to
        do when an object of this
        class is called directly.
        """
        if self.total_time:
            print(f"{self.name} total time: {round(self.total_time, 2)}s")
        else:
            print("There is no recorded time.")
    
    def __len__(self):
        """
        Tells the interpreter what to
        consider this class' length.
        """
        if self.total_time // 60 == 1:
            return int(self.total_time // 60)
        elif self.total_time // 3600 == 1:
            return int(self.total_time // 3600)
        else:
            return int(self.total_time)

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


    def start(self):
        """
        Starts the timer by
        initializing an object attribute.
        """
        self._start_time = time()


    def pause(self, duration: float = None):
        """
        Pauses the timer.
        """
        self._pause_time = time()
        if duration:
            sleep(duration)


    def resume(self):
        """
        Resumes the timer.
        """
        if self._paused_time:
            self._paused_time += self._calculate_time(self._pause_time, time())
        else:
            self._paused_time = self._calculate_time(self._pause_time, time())


    def stop(self):
        """
        Stops the timer and calculates
        the total time passed.
        """
        if self._pause_time and not self._paused_time: # if stopped while paused
            self.resume()
        self._stop_time = time()
        self.total_time = self._calculate_time(self._start_time, self._stop_time)


    def _calculate_time(self, time1: float, time2: float) -> float:
        """
        Returns the difference in time where t2>t1.
        """
        return time2 - time1


    def reset(self):
        """
        Resets all timer attributes.
        """
        self._start_time = None
        self._pause_time = None
        self._paused_time = None
        self._stop_time = None
        self.total_time = None
