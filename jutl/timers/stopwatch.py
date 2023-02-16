# Module imports
from time import time

# External class visibility
__all__ = ['Stopwatch']


class Stopwatch():
    """
    Class which acts as a stopwatch
    with time and lap methods.
    """
    def __init__(self, name: str = None):
        "Initialization method."
        self.name: str = name
        self._start_time: float
        self._stop_time: float
        self.total_time: float = None
        self._laps: list[float] = []
        self.lap_times: list[float] = []

    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.name is None:
            if self.total_time is None:
                return "Stopwatch()"
            else:
                return f"Stopwatch({round(self.total_time, 2)}s)"
        else:
            if self.total_time is None:
                return f"Stopwatch({self.name})"
            else:
                return f"Stopwatch({self.name}, {round(self.total_time, 2)}s)"

    def __call__(self):
        """
        Tells the interpreter what to
        do when an object of this
        class is called directly.
        """
        if self.lap_times:
            for n, time in enumerate(self.lap_times):
                print(f"Lap {n+1}: {round(time, 2)}s")
        else:
            print("There are no lap times.")

    def __len__(self) -> int:
        """
        Tells the interpreter what to
        consider this class' length.
        """
        return len(self._laps)

    def __iter__(self) -> iter:
        """
        Tells the interpreter what to
        iterate over when iterator methods
        are called on this class.
        """
        return iter(self.lap_times)

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
        Starts the stopwatch by
        initializing an object attribute.
        """
        self._start_time = time()


    def lap(self, lap_time: float = None):
        """
        Adds the current time to the lap time
        list and records the time since the
        start or time of the last recorded lap.
        """
        if lap_time:
            self._laps.append(lap_time)
        else:
            self._laps.append(time())
        if not self.lap_times:
            self.lap_times.append(self._calculate_time(self._start_time, self._laps[-1]))
        else:
            self.lap_times.append(self._calculate_time(self._laps[-2], self._laps[-1]))


    def stop(self):
        """
        Stops the stopwatch and calculates
        the total time passed.
        """
        self._stop_time = time()
        self.total_time = self._calculate_time(self._start_time, self._stop_time)
        self.lap(self._stop_time)


    def _calculate_time(self, time1: float, time2: float) -> float:
        """
        Returns the difference in time where t2>t1.
        """
        return time2 - time1


    def reset(self):
        """
        Resets all stopwatch attributes.
        """
        self._start_time = None
        self._stop_time = None
        self.total_time = None
        self._laps.clear()
        self.lap_times.clear()
