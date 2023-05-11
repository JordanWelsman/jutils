# jutils/test/timers/test_reporter.py
from jutl.timers import Reporter
from time import sleep

test_name: str = "Test name"

class TestInit():
    def test_def(self):
        "Tests if an object can be created from the Reporter class."
        reporter = Reporter()
        assert isinstance(reporter, Reporter)
        del(reporter)
  
    def test_name(self):
        "Tests if naming a reporter works."
        reporter = Reporter()
        assert reporter.name is None
        del(reporter)

        reporter = Reporter(test_name)
        assert reporter.name == test_name
        del(reporter)


class TestDunder():
    def test_repr(self):
        "Tests what is output for representation."
        reporter = Reporter()
        assert repr(reporter) == f"Reporter()"
        del(reporter)

        reporter = Reporter()
        reporter.start()
        reporter.stop()
        assert repr(reporter) == f"Reporter({round(reporter.total_time, 2)}s)"
        del(reporter)

        reporter = Reporter(test_name)
        assert repr(reporter) == f"Reporter({test_name})"
        del(reporter)

        reporter = Reporter(test_name)
        reporter.start()
        reporter.stop()
        assert repr(reporter) == f"Reporter({test_name}, {round(reporter.total_time, 2)}s)"
        del(reporter)

    def test_len(self):
        "Tests what is output for object length."
        reporter = Reporter()
        reporter.start()
        reporter.stop()
        assert len(reporter) == 1
        del(reporter)

        reporter = Reporter()
        reporter.start()
        reporter.loop()
        reporter.stop()
        assert len(reporter) == 2
        del(reporter)

        reporter = Reporter()
        reporter.start()
        reporter.loop()
        reporter.loop()
        reporter.stop()
        assert len(reporter) == 3
        del(reporter)

    def test_iter(self):
        "Tests object's iteration reporting."
        reporter = Reporter()
        reporter.start()
        reporter.stop()
        reporter_iter = iter(reporter)
        assert next(reporter_iter) == reporter.total_time
        del(reporter)
        del(reporter_iter)

        reporter = Reporter()
        reporter.start()
        reporter.loop()
        reporter.loop()
        reporter.loop()
        reporter.stop()
        reporter_iter = iter(reporter)
        assert next(reporter_iter) == reporter.loop_times[0]
        assert next(reporter_iter) == reporter.loop_times[1]
        assert next(reporter_iter) == reporter.loop_times[2]
        assert next(reporter_iter) == reporter.loop_times[3]
        del(reporter)
        del(reporter_iter)

    def test_equal(self):
        "Tests the overridden equal function."
        reporter1 = Reporter()
        reporter1.start()
        reporter1.stop()
        reporter2 = reporter1
        assert reporter1 == reporter2
        del(reporter1)
        del(reporter2)

    def test_not_equal(self):
        "Tests the overridden not equal function."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter1 != reporter2
        del(reporter1)
        del(reporter2)

    def test_greater_than(self):
        "Tests the overridden greater than function."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter1 > reporter2
        del(reporter1)
        del(reporter2)

    def test_greater_equal(self):
        "Tests the overridden greater or equal function."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter1 > reporter2
        del(reporter1)
        del(reporter2)

        reporter1 = Reporter()
        reporter1.start()
        reporter1.stop()
        reporter2 = reporter1
        assert reporter1 == reporter2
        del(reporter1)
        del(reporter2)

    def test_less_than(self):
        "Tests the overridden less than function."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter2 < reporter1
        del(reporter1)
        del(reporter2)

    def test_less_equal(self):
        "Tests the overridden less or equal function."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter2 < reporter1
        del(reporter1)
        del(reporter2)

        reporter1 = Reporter()
        reporter1.start()
        reporter1.stop()
        reporter2 = reporter1
        assert reporter1 == reporter2
        del(reporter1)
        del(reporter2)

    def test_add(self):
        "Tests the sum operator."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter1 + reporter2 == reporter1.total_time + reporter2.total_time
        del(reporter1)
        del(reporter2)

    def test_sub(self):
        "Tests the subtract operator."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.01)
        reporter1.stop()
        reporter2.start()
        reporter2.stop()
        assert reporter1 - reporter2 == reporter1.total_time - reporter2.total_time
        del(reporter1)
        del(reporter2)

    def test_mul(self):
        "Tests the multiply operator."
        reporter = Reporter()
        reporter.start()
        sleep(0.01)
        reporter.stop()
        assert reporter * 2 == reporter.total_time * 2
        del(reporter)

    def test_truediv(self):
        "Tests the divide operator."
        reporter1 = Reporter()
        reporter2 = Reporter()
        reporter1.start()
        sleep(0.02)
        reporter1.stop()
        reporter2.start()
        sleep(0.01)
        reporter2.stop()
        assert reporter1 / reporter2 == reporter1.total_time / reporter2.total_time
        del(reporter1)
        del(reporter2)


class TestRobustness():
    def test_equal_list_sizes(self):
        """
        Checks recorded loop time and loop
        difference lists are equally sized.
        """
        reporter = Reporter()
        assert len(reporter._loops) == len(reporter.loop_times)
        del(reporter)

        reporter = Reporter()
        reporter.start()
        reporter.stop()
        assert len(reporter._loops) == len(reporter.loop_times)
        del(reporter)

        reporter = Reporter()
        reporter.start()
        reporter.loop()
        reporter.loop()
        reporter.loop()
        reporter.stop()
        assert len(reporter._loops) == len(reporter.loop_times)
        del(reporter)
    
    def test_stop_accuracy(self):
        """
        Checks accuracy of
        calculate_time() method.
        """
        reporter = Reporter()
        reporter.start()
        sleep(0.1)
        reporter.stop()
        assert 0.100 <= reporter.total_time <= 0.110 # within 10ms tolerance
        del(reporter)
