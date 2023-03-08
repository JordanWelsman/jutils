# jutils/test/datastructures/test_queue.py
from jutl.datastructures import Queue

test_name = "Test name"
test_item = "Item"

class TestInit():
    def test_def(self):
        "Tests if an object can be created from the Queue class."
        queue = Queue()
        assert isinstance(queue, Queue)
        del(queue)

    def test_name(self):
        "Tests if naming a queue works."
        queue = Queue()
        assert queue.name is None
        del(queue)

        queue = Queue(test_name)
        assert queue.name == test_name
        del(queue)


class TestDunder():
    def test_repr(self):
        "Tests what is output for representation."
        queue = Queue()
        assert repr(queue) == f"Queue()"
        del(queue)

        queue = Queue(test_name)
        assert repr(queue) == f"Queue({test_name})"
        del(queue)

        queue = Queue()
        queue.enqueue(test_item, test_item, test_item)
        assert repr(queue) == f"Queue(3)"
        del(queue)

        queue = Queue(capacity=10)
        assert repr(queue) == f"Queue(10)"
        del(queue)

        queue = Queue(test_name)
        queue.enqueue(test_item, test_item, test_item)
        assert repr(queue) == f"Queue({test_name}, 3)"
        del(queue)

        queue = Queue(test_name, 10)
        assert repr(queue) == f"Queue({test_name}, 10)"
        del(queue)

        queue = Queue(test_name, 10)
        queue.enqueue(test_item, test_item, test_item)
        assert repr(queue) == f"Queue({test_name}, 3/10)"
        del(queue)


    def test_len(self):
        "Tests what is output for object length."
        queue = Queue()
        assert len(queue) == 0
        del(queue)

        queue = Queue()
        queue.enqueue(test_item)
        assert len(queue) == 1
        del(queue)

        queue = Queue()
        queue.enqueue(test_item)
        queue.enqueue(test_item)
        assert len(queue) == 2
        del(queue)

        queue = Queue()
        queue.enqueue(test_item, test_item, test_item)
        assert len(queue) == 3
        del(queue)

    def test_equal(self):
        "Tests the overridden equal function."
        stack1 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2 = Queue()
        stack2.enqueue(test_item, test_item, test_item)
        assert stack1 == stack2
        del(stack1)
        del(stack2)

    def test_not_equal(self):
        "Tests the overridden not equal function."
        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item)
        assert stack1 != stack2
        del(stack1)
        del(stack2)

    def test_greater_than(self):
        "Tests the overridden greater than function."
        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item)
        assert stack1 > stack2
        del(stack1)
        del(stack2)

    def test_greater_equal(self):
        "Tests the overridden greater or equal function."
        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item)
        assert stack1 >= stack2
        del(stack1)
        del(stack2)

        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item, test_item)
        assert stack1 >= stack2
        del(stack1)
        del(stack2)

    def test_less_than(self):
        "Tests the overridden less than function."
        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item)
        assert stack2 < stack1
        del(stack1)
        del(stack2)

    def test_less_equal(self):
        "Tests the overridden less or equal function."
        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item)
        assert stack2 <= stack1
        del(stack1)
        del(stack2)

        stack1 = Queue()
        stack2 = Queue()
        stack1.enqueue(test_item, test_item, test_item)
        stack2.enqueue(test_item, test_item, test_item)
        assert stack1 <= stack2
        del(stack1)
        del(stack2)

    def test_add(self):
        "Tests the sum operator."
        stack1 = Queue()
        stack2 = Queue()
        stack3 = Queue()
        test_stack = Queue()
        stack1.enqueue(test_item, test_item)
        stack2.enqueue(test_item, test_item)
        stack3.enqueue(test_item, test_item)
        test_stack.enqueue(test_item, test_item, test_item, test_item, test_item, test_item)
        assert stack1 + stack2 + stack3 == test_stack
        del(stack1)
        del(stack2)
        del(stack3)
        del(test_stack)


class TestRobustness():
    def test_push(self):
        """
        Checks if pushing an
        item to a queue works.
        """
        queue = Queue()
        queue.enqueue(test_item)
        assert len(queue) == 1
        del(queue)

        queue = Queue()
        queue.enqueue(test_item)
        queue.enqueue(test_item)
        assert len(queue) == 2
        del(queue)

        queue = Queue()
        queue.enqueue(test_item, test_item, test_item)
        assert len(queue) == 3
        del(queue)

    def test_pop(self):
        """
        Checks if popping an
        item from a queue works.
        """
        queue = Queue()
        queue.enqueue(test_item, test_item, test_item)
        assert queue.dequeue() == test_item
        assert len(queue) == 2
        del(queue)

        queue = Queue()
        queue.enqueue(test_item)
        assert queue.dequeue() == test_item
        assert len(queue) == 0
        del(queue)

    def test_extend(self):
        """
        Checks if the extend
        method works correctly.
        """
        stack1 = Queue()
        stack2 = Queue()
        test_stack = Queue()
        stack1.enqueue(test_item, test_item)
        stack2.enqueue(test_item, test_item)
        test_stack.enqueue(test_item, test_item, test_item, test_item)
        assert stack1.extend(stack2) == test_stack

