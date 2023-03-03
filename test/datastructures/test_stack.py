# jutils/test/datastructures/test_stack.py
from jutl.datastructures import Stack
from time import sleep

test_name = "Test name"
test_item = "Item"

class TestInit():
    def test_def(self):
        "Tests if an object can be created from the Stack class."
        stack = Stack()
        assert isinstance(stack, Stack)
        del(stack)

    def test_name(self):
        "Tests if naming a stack works."
        stack = Stack()
        assert stack.name is None
        del(stack)

        stack = Stack(test_name)
        assert stack.name == test_name
        del(stack)
    
class TestDunder():
    def test_repr(self):
        "Tests what is output for representation."
        stack = Stack()
        assert repr(stack) == f"Stack()"
        del(stack)

        stack = Stack()
        stack.push(test_item)
        assert repr(stack) == f"Stack(['Item'])"
        del(stack)

        stack = Stack(test_name)
        assert repr(stack) == f"Stack({test_name})"
        del(stack)

        stack = Stack(test_name)
        stack.push(test_item)
        assert repr(stack) == f"Stack({test_name}, ['Item'])"
        del(stack)

    def test_len(self):
        "Tests what is output for object length."
        stack = Stack()
        assert len(stack) == 0
        del(stack)

        stack = Stack()
        stack.push(test_item)
        assert len(stack) == 1
        del(stack)

        stack = Stack()
        stack.push(test_item)
        stack.push(test_item)
        assert len(stack) == 2
        del(stack)

        stack = Stack()
        stack.push(test_item, test_item, test_item)
        assert len(stack) == 3
        del(stack)

    def test_equal(self):
        "Tests the overridden equal function."
        stack1 = Stack()
        stack1.start()
        stack1.stop()
        stack2 = stack1
        assert stack1 == stack2
        del(stack1)
        del(stack2)

    def test_not_equal(self):
        "Tests the overridden not equal function."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack1 != stack2
        del(stack1)
        del(stack2)

    def test_greater_than(self):
        "Tests the overridden greater than function."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack1 > stack2
        del(stack1)
        del(stack2)

    def test_greater_equal(self):
        "Tests the overridden greater or equal function."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack1 > stack2
        del(stack1)
        del(stack2)

        stack1 = Stack()
        stack1.start()
        stack1.stop()
        stack2 = stack1
        assert stack1 == stack2
        del(stack1)
        del(stack2)

    def test_less_than(self):
        "Tests the overridden less than function."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack2 < stack1
        del(stack1)
        del(stack2)

    def test_less_equal(self):
        "Tests the overridden less or equal function."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack2 < stack1
        del(stack1)
        del(stack2)

        stack1 = Stack()
        stack1.start()
        stack1.stop()
        stack2 = stack1
        assert stack1 == stack2
        del(stack1)
        del(stack2)

    def test_add(self):
        "Tests the sum operator."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack1 + stack2 == stack1.total_time + stack2.total_time
        del(stack1)
        del(stack2)

    def test_sub(self):
        "Tests the subtract operator."
        stack1 = Stack()
        stack2 = Stack()
        stack1.start()
        sleep(0.01)
        stack1.stop()
        stack2.start()
        stack2.stop()
        assert stack1 - stack2 == stack1.total_time - stack2.total_time
        del(stack1)
        del(stack2)
