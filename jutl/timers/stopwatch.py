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
    self.name : str = name
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
    if self._laps:
      self.lap(self._stop_time)


  def _calculate_time(self, t1: float, t2: float) -> float:
    """
    Returns the difference in time where t2>t1.
    """
    return t2 - t1
