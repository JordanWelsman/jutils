# jutils/test/pipelining/test_instructionpipeline.py
from jutl.pipelining import InstructionPipeline
from jutl.exceptions import EmptyPipelineError, MissingInputError

test_name: str = "Test name"
def func(num):
    return num+1

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
        del(pipeline)

        pipeline = InstructionPipeline(name=test_name)
        assert pipeline.name == test_name
        del(pipeline)


class TestDunder():
    def test_repr(self):
        "Tests what is output for representation."
        pipeline = InstructionPipeline()
        assert repr(pipeline) == "InstructionPipeline()"
        del(pipeline)

        pipeline = InstructionPipeline(func)
        assert repr(pipeline) == f"InstructionPipeline({len(pipeline.functions)})"
        del(pipeline)

        pipeline = InstructionPipeline(name=test_name)
        assert repr(pipeline) == f"InstructionPipeline({test_name})"
        del(pipeline)

        pipeline = InstructionPipeline(func, name=test_name)
        assert repr(pipeline) == f"InstructionPipeline({test_name}, {len(pipeline.functions)})"
        del(pipeline)

    def test_len(self):
        "Tests what is output for object length."
        pipeline = InstructionPipeline()
        assert len(pipeline) == 0
        del(pipeline)

        pipeline = InstructionPipeline(func)
        assert len(pipeline) == 1
        del(pipeline)

        pipeline = InstructionPipeline(func, func)
        assert len(pipeline) == 2
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func)
        assert len(pipeline) == 3
        del(pipeline)

    def test_iter(self):
        "Tests object's iteration reporting."
        pipeline = InstructionPipeline(func)
        pipeline_iter = iter(pipeline)
        assert next(pipeline_iter) == pipeline.functions[0]
        del(pipeline)
        del(pipeline_iter)

        pipeline = InstructionPipeline(func, func, func, func)
        pipeline_iter = iter(pipeline)
        assert next(pipeline_iter) == pipeline.functions[0]
        assert next(pipeline_iter) == pipeline.functions[1]
        assert next(pipeline_iter) == pipeline.functions[2]
        assert next(pipeline_iter) == pipeline.functions[3]
        del(pipeline)
        del(pipeline_iter)

    def test_call(self):
        "Tests what is output when object is called."
        pipeline = InstructionPipeline()
        try:
            pipeline(1)
        except EmptyPipelineError:
            pass
        else: assert False, "Expected an EmptyPipelineError."
        del(pipeline)

        pipeline = InstructionPipeline(func)
        try:
            pipeline()
        except MissingInputError:
            pass
        else: assert False, "Expected a MissingInputError."
        del(pipeline)

        pipeline = InstructionPipeline(func)
        assert pipeline(1) == 2
        del(pipeline)

        pipeline = InstructionPipeline(func, func)
        assert pipeline(1) == 3
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func)
        assert pipeline(1) == 4
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func, func)
        assert pipeline(1) == 5
        del(pipeline)


class TestMethods():
    def test_add_function(self):
        "Tests adding a function to the pipeline."
        pipeline = InstructionPipeline()
        pipeline.add(func)
        assert len(pipeline.functions) == 1
        del(pipeline)

        pipeline = InstructionPipeline(func)
        pipeline.add(func)
        assert len(pipeline.functions) == 2
        del(pipeline)

        pipeline = InstructionPipeline(func, func)
        pipeline.add(func)
        assert len(pipeline.functions) == 3
        del(pipeline)

        pipeline = InstructionPipeline(func, func)
        pipeline.add(func)
        pipeline.add(func)
        assert len(pipeline.functions) == 4
        del(pipeline)

        pipeline = InstructionPipeline(func, func)
        pipeline.add(func, func, func)
        assert len(pipeline.functions) == 5
        del(pipeline)

    def test_remove_function(self):
        "Tests removing a function from the pipeline."
        pipeline = InstructionPipeline()
        pipeline.remove(func)
        assert len(pipeline.functions) == 0
        del(pipeline)
        
        pipeline = InstructionPipeline()
        pipeline.add(func)
        pipeline.remove(func)
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func)
        pipeline.remove(func)
        assert len(pipeline.functions) == 2
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func)
        pipeline.remove(func)
        pipeline.remove(func)
        assert len(pipeline.functions) == 1
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func, func)
        pipeline.remove(func, func, func)
        assert len(pipeline.functions) == 1
        del(pipeline)

    def test_clear(self):
        "Tests clearing the pipeline."
        pipeline = InstructionPipeline()
        pipeline.add(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = InstructionPipeline()
        pipeline.add(func)
        pipeline.add(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = InstructionPipeline(func, func)
        pipeline.add(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = InstructionPipeline(func, func, func, func)
        pipeline.add(func, func)
        pipeline.remove(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)
