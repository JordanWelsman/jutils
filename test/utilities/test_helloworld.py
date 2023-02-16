# jutils/test/utilities/test_helloworld.py
from jutl.utilities import hello_world

test_name: str = "Test name"

class TestFunction():
    def test_call_without_name(self):
        assert hello_world() == "Hello, World!"
    
    def test_call_with_name(self):
        assert hello_world(test_name) == f"Hello, {test_name}!"