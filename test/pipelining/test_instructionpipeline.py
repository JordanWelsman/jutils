# jutils/test/pipelining/test_instructionpipeline.py
from jutl.pipelining import InstructionPipeline

test_name: str = "Test name"

class TestInit():
    def test_def(self):
        "Tests if an object can be created from the InstructionPipeline class."
        pipeline = InstructionPipeline()
        assert isinstance(pipeline, InstructionPipeline)
        del(pipeline)

    def test_name(self):
        "Tests if naming a pipeline works."
        pipeline = InstructionPipeline()
        assert pipeline.name is None


        pipeline = InstructionPipeline(name=test_name)
        assert pipeline.name == test_name
        del(pipeline)
