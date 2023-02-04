# jutils/test/timers/test_timer.py
from jutl.timers import Timer
from time import sleep

test_name: str = "Test name"

class TestInit():
  def test_def(self):
    "Tests if an object can be created from the Timer class."
    timer = Timer()
    assert timer is not None
    del(timer)

  def test_name(self):
    "Tests if naming a timer works."
    timer = Timer()
    assert timer.name == None
    del(timer)

    timer = Timer(test_name)
    assert timer.name == test_name
    del(timer)


class TestDunder():
  def test_repr(self):
    "Tests what is output for representation."
    timer = Timer()
    assert repr(timer) == f"Timer()"
    del(timer)

    timer = Timer()
    timer.start()
    timer.stop()
    assert repr(timer) == f"Timer({round(timer.total_time, 2)}s)"
    del(timer)

    timer = Timer(test_name)
    assert repr(timer) == f"Timer({test_name})"
    del(timer)

    timer = Timer(test_name)
    timer.start()
    timer.stop()
    assert repr(timer) == f"Timer({test_name}, {round(timer.total_time, 2)}s)"
    del(timer)

  def test_len(self):
    "Tests what is output for object length."
    timer = Timer()
    timer.start()
    timer.stop()
    assert len(timer) == 0
    del(timer)
  
  def test_equal(self):
    "Tests the overridden equal function."
    timer1 = Timer()
    timer1.start()
    timer1.stop()
    timer2 = timer1
    assert timer1 == timer2
    del(timer1)
    del(timer2)

  def test_not_equal(self):
    "Tests the overridden not equal function."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer1 != timer2
    del(timer1)
    del(timer2)

  def test_greater_than(self):
    "Tests the overridden greater than function."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer1 > timer2
    del(timer1)
    del(timer2)

  def test_greater_equal(self):
    "Tests the overridden greater or equal function."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer1 > timer2
    del(timer1)
    del(timer2)

    timer1 = Timer()
    timer1.start()
    timer1.stop()
    timer2 = timer1
    assert timer1 == timer2
    del(timer1)
    del(timer2)

  def test_less_than(self):
    "Tests the overridden less than function."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer2 < timer1
    del(timer1)
    del(timer2)

  def test_less_equal(self):
    "Tests the overridden less or equal function."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer2 < timer1
    del(timer1)
    del(timer2)

    timer1 = Timer()
    timer1.start()
    timer1.stop()
    timer2 = timer1
    assert timer1 == timer2
    del(timer1)
    del(timer2)

  def test_add(self):
    "Tests the sum operator."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer1 + timer2 == timer1.total_time + timer2.total_time
    del(timer1)
    del(timer2)

  def test_sub(self):
    "Tests the subtract operator."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    timer2.start()
    timer2.stop()
    assert timer1 - timer2 == timer1.total_time - timer2.total_time
    del(timer1)
    del(timer2)

  def test_mul(self):
    "Tests the multiply operator."
    timer1 = Timer()
    timer1.start()
    sleep(0.01)
    timer1.stop()
    assert timer1 * 2 == timer1.total_time * 2
    del(timer1)

  def test_truediv(self):
    "Tests the divide operator."
    timer1 = Timer()
    timer2 = Timer()
    timer1.start()
    sleep(0.02)
    timer1.stop()
    timer2.start()
    sleep(0.01)
    timer2.stop()
    assert timer1 / timer2 == timer1.total_time / timer2.total_time
    del(timer1)
    del(timer2)


class TestRobustness():
  def test_pause_resume(self):
    """
    Checks the pause and
    resume methods work.
    """
    timer = Timer()
    timer.start()
    timer.pause()
    timer.resume()
    timer.stop()
    assert timer.total_time > 0
    del(timer)

  def test_multiple_pause(self):
    """
    Checks correct time is calculated
    with mulitple pauses & resumes.
    """
    timer = Timer()
    timer.start()
    timer.pause()
    timer.resume()
    timer.pause()
    timer.resume()
    timer.pause()
    timer.resume()
    timer.stop()
    assert timer.total_time > 0
    del(timer)

  def test_pause_wait(self):
    """
    Checks passed wait time
    correctly executes.
    """
    timer = Timer()
    timer.start()
    timer.pause(0.1)
    timer.resume()
    timer.stop()
    assert timer._paused_time >= 0.1
    del(timer)
  
  def test_early_stop(self):
    """
    Checks the timer correctly
    stops if stopped while paused.
    """
    timer = Timer()
    timer.start()
    timer.pause()
    timer.stop()
    assert timer._pause_time
    assert timer._paused_time
    del(timer)

  def test_stop_accuracy(self):
    """
    Checks accuracy of
    calculate_time() method.
    """
    timer = Timer()
    timer.start()
    sleep(0.1)
    timer.stop()
    assert 0.100 <= timer.total_time <= 0.110 # within 10ms tolerance
    del(timer)
