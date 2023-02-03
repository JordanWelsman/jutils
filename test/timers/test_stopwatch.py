# jutils/test/timers/test_stopwatch.py
from jutl.timers import Stopwatch

test_name: str = "Test name"

class TestInit():
  def test_def(self):
    "Tests if an object can be created from the Stopwatch class."
    stopwatch = Stopwatch()
    assert stopwatch is not None
    del(stopwatch)
  
  def test_name(self):
    "Tests if naming a stopwatch works."
    stopwatch = Stopwatch()
    assert stopwatch.name == None
    del(stopwatch)

    stopwatch = Stopwatch(test_name)
    assert stopwatch.name == test_name
    del(stopwatch)


class TestDunder():
  def test_repr(self):
    "Tests what is output for representation."
    stopwatch = Stopwatch()
    assert repr(stopwatch) == f"Stopwatch()"
    del(stopwatch)

    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.stop()
    assert repr(stopwatch) == f"Stopwatch({round(stopwatch.total_time, 2)}s)"
    del(stopwatch)

    stopwatch = Stopwatch(test_name)
    assert repr(stopwatch) == f"Stopwatch({test_name})"
    del(stopwatch)

    stopwatch = Stopwatch(test_name)
    stopwatch.start()
    stopwatch.stop()
    assert repr(stopwatch) == f"Stopwatch({test_name}, {round(stopwatch.total_time, 2)}s)"
    del(stopwatch)

  def test_len(self):
    "Tests what is output for object length."
    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.stop()
    assert len(stopwatch) == 1
    del(stopwatch)

    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.lap()
    stopwatch.stop()
    assert len(stopwatch) == 2
    del(stopwatch)

    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.lap()
    stopwatch.lap()
    stopwatch.stop()
    assert len(stopwatch) == 3
    del(stopwatch)

  def test_iter(self):
    "Tests object's iteration reporting."
    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.stop()
    stopwatch_iter = iter(stopwatch)
    assert next(stopwatch_iter) == stopwatch.total_time
    del(stopwatch)
    del(stopwatch_iter)

    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.lap()
    stopwatch.lap()
    stopwatch.lap()
    stopwatch.stop()
    stopwatch_iter = iter(stopwatch)
    assert next(stopwatch_iter) == stopwatch.lap_times[0]
    assert next(stopwatch_iter) == stopwatch.lap_times[1]
    assert next(stopwatch_iter) == stopwatch.lap_times[2]
    assert next(stopwatch_iter) == stopwatch.lap_times[3]
    del(stopwatch)
    del(stopwatch_iter)
