# jutils/test/timers/test_stopwatch.py
from jutl.timers import Stopwatch
from time import sleep

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

  def test_equal(self):
    "Tests the overridden equal function."
    stopwatch1 = Stopwatch()
    stopwatch1.start()
    stopwatch1.stop()
    stopwatch2 = stopwatch1
    assert stopwatch1 == stopwatch2
    del(stopwatch1)
    del(stopwatch2)

  def test_not_equal(self):
    "Tests the overridden not equal function."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch1 != stopwatch2
    del(stopwatch1)
    del(stopwatch2)

  def test_greater_than(self):
    "Tests the overridden greater than function."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch1 > stopwatch2
    del(stopwatch1)
    del(stopwatch2)

  def test_greater_equal(self):
    "Tests the overridden greater or equal function."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch1 > stopwatch2
    del(stopwatch1)
    del(stopwatch2)

    stopwatch1 = Stopwatch()
    stopwatch1.start()
    stopwatch1.stop()
    stopwatch2 = stopwatch1
    assert stopwatch1 == stopwatch2
    del(stopwatch1)
    del(stopwatch2)

  def test_less_than(self):
    "Tests the overridden less than function."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch2 < stopwatch1
    del(stopwatch1)
    del(stopwatch2)

  def test_less_equal(self):
    "Tests the overridden less or equal function."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch2 < stopwatch1
    del(stopwatch1)
    del(stopwatch2)

    stopwatch1 = Stopwatch()
    stopwatch1.start()
    stopwatch1.stop()
    stopwatch2 = stopwatch1
    assert stopwatch1 == stopwatch2
    del(stopwatch1)
    del(stopwatch2)

  def test_add(self):
    "Tests the sum operator."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch1 + stopwatch2 == stopwatch1.total_time + stopwatch2.total_time
    del(stopwatch1)
    del(stopwatch2)

  def test_sub(self):
    "Tests the subtract operator."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.01)
    stopwatch1.stop()
    stopwatch2.start()
    stopwatch2.stop()
    assert stopwatch1 - stopwatch2 == stopwatch1.total_time - stopwatch2.total_time
    del(stopwatch1)
    del(stopwatch2)

  def test_mul(self):
    "Tests the multiply operator."
    stopwatch = Stopwatch()
    stopwatch.start()
    sleep(0.01)
    stopwatch.stop()
    assert stopwatch * 2 == stopwatch.total_time * 2
    del(stopwatch)

  def test_truediv(self):
    "Tests the divide operator."
    stopwatch1 = Stopwatch()
    stopwatch2 = Stopwatch()
    stopwatch1.start()
    sleep(0.02)
    stopwatch1.stop()
    stopwatch2.start()
    sleep(0.01)
    stopwatch2.stop()
    assert stopwatch1 / stopwatch2 == stopwatch1.total_time / stopwatch2.total_time
    del(stopwatch1)
    del(stopwatch2)


class TestRobustness():
  def test_equal_list_sizes(self):
    """
    Checks recorded lap time and lap
    difference lists are equally sized.
    """
    stopwatch = Stopwatch()
    assert len(stopwatch._laps) == len(stopwatch.lap_times)
    del(stopwatch)

    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.stop()
    assert len(stopwatch._laps) == len(stopwatch.lap_times)
    del(stopwatch)

    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.lap()
    stopwatch.lap()
    stopwatch.lap()
    stopwatch.stop()
    assert len(stopwatch._laps) == len(stopwatch.lap_times)
    del(stopwatch)
    
  def test_stop_accuracy(self):
    """
    Checks accuracy of
    calculate_time() method.
    """
    stopwatch = Stopwatch()
    stopwatch.start()
    sleep(0.1)
    stopwatch.stop()
    assert 0.100 <= stopwatch.total_time <= 0.110 # within 10ms tolerance
    del(stopwatch)
