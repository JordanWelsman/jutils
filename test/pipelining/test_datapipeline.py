# jutils/test/pipelining/test_datapipeline.py
from jutl.pipelining import DataPipeline
from jutl.exceptions import EmptyPipelineError, MissingInputError

test_name: str = "Test name"
def func(num):
    return num+1

class TestInit():
    def test_def(self):
        "Tests if an object can be created from the DataPipeline class."
        pipeline = DataPipeline()
        assert isinstance(pipeline, DataPipeline)
        del(pipeline)

    def test_name(self):
        "Tests if naming a pipeline works."
        pipeline = DataPipeline()
        assert pipeline.name is None
        del(pipeline)

        pipeline = DataPipeline(name=test_name)
        assert pipeline.name == test_name
        del(pipeline)


class TestDunder():
    def test_repr(self):
        "Tests what is output for representation."
        pipeline = DataPipeline()
        assert repr(pipeline) == "DataPipeline()"
        del(pipeline)

        pipeline = DataPipeline(func)
        assert repr(pipeline) == f"DataPipeline({len(pipeline.functions)})"
        del(pipeline)

        pipeline = DataPipeline(name=test_name)
        assert repr(pipeline) == f"DataPipeline({test_name})"
        del(pipeline)

        pipeline = DataPipeline(func, name=test_name)
        assert repr(pipeline) == f"DataPipeline({test_name}, {len(pipeline.functions)})"
        del(pipeline)

    def test_len(self):
        "Tests what is output for object length."
        pipeline = DataPipeline()
        assert len(pipeline) == 0
        del(pipeline)

        pipeline = DataPipeline(func)
        assert len(pipeline) == 1
        del(pipeline)

        pipeline = DataPipeline(func, func)
        assert len(pipeline) == 2
        del(pipeline)

        pipeline = DataPipeline(func, func, func)
        assert len(pipeline) == 3
        del(pipeline)

    def test_iter(self):
        "Tests object's iteration reporting."
        pipeline = DataPipeline(func)
        pipeline_iter = iter(pipeline)
        assert next(pipeline_iter) == pipeline.functions[0]
        del(pipeline)
        del(pipeline_iter)

        pipeline = DataPipeline(func, func, func, func)
        pipeline_iter = iter(pipeline)
        assert next(pipeline_iter) == pipeline.functions[0]
        assert next(pipeline_iter) == pipeline.functions[1]
        assert next(pipeline_iter) == pipeline.functions[2]
        assert next(pipeline_iter) == pipeline.functions[3]
        del(pipeline)
        del(pipeline_iter)

    def test_call_single(self):
        "Tests what is output when object is called with single input."
        pipeline = DataPipeline()
        try:
            pipeline(1)
        except EmptyPipelineError:
            pass
        else: assert False, "Expected an EmptyPipelineError."
        del(pipeline)

        pipeline = DataPipeline(func)
        try:
            pipeline()
        except MissingInputError:
            pass
        else: assert False, "Expected a MissingInputError."
        del(pipeline)

        pipeline = DataPipeline(func)
        assert pipeline(1) == [2]
        del(pipeline)

        pipeline = DataPipeline(func, func)
        assert pipeline(1) == [3]
        del(pipeline)

        pipeline = DataPipeline(func, func, func)
        assert pipeline(1) == [4]
        del(pipeline)

        pipeline = DataPipeline(func, func, func, func)
        assert pipeline(1) == [5]
        del(pipeline)

    def test_call_multiple(self):
        "Tests what is output when object is called with multiple inputs."
        pipeline = DataPipeline()
        try:
            pipeline(1)
        except EmptyPipelineError:
            pass
        else: assert False, "Expected an EmptyPipelineError."
        del(pipeline)

        pipeline = DataPipeline(func)
        try:
            pipeline()
        except MissingInputError:
            pass
        else: assert False, "Expected a MissingInputError."
        del(pipeline)

        pipeline = DataPipeline(func)
        assert pipeline(1, 2, 3) == [2, 3, 4]
        del(pipeline)

        pipeline = DataPipeline(func, func)
        assert pipeline(1, 2, 3) == [3, 4, 5]
        del(pipeline)

        pipeline = DataPipeline(func, func, func)
        assert pipeline(1, 2, 3) == [4, 5, 6]
        del(pipeline)

        pipeline = DataPipeline(func, func, func, func)
        assert pipeline(1, 2, 3) == [5, 6, 7]
        del(pipeline)


class TestMethods():
    def test_add_function(self):
        "Tests adding a function to the pipeline."
        pipeline = DataPipeline()
        pipeline.add(func)
        assert len(pipeline.functions) == 1
        del(pipeline)

        pipeline = DataPipeline(func)
        pipeline.add(func)
        assert len(pipeline.functions) == 2
        del(pipeline)

        pipeline = DataPipeline(func, func)
        pipeline.add(func)
        assert len(pipeline.functions) == 3
        del(pipeline)

        pipeline = DataPipeline(func, func)
        pipeline.add(func)
        pipeline.add(func)
        assert len(pipeline.functions) == 4
        del(pipeline)

        pipeline = DataPipeline(func, func)
        pipeline.add(func, func, func)
        assert len(pipeline.functions) == 5
        del(pipeline)

    def test_remove_function(self):
        "Tests removing a function from the pipeline."
        pipeline = DataPipeline()
        pipeline.remove(func)
        assert len(pipeline.functions) == 0
        del(pipeline)
        
        pipeline = DataPipeline()
        pipeline.add(func)
        pipeline.remove(func)
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = DataPipeline(func, func, func)
        pipeline.remove(func)
        assert len(pipeline.functions) == 2
        del(pipeline)

        pipeline = DataPipeline(func, func, func)
        pipeline.remove(func)
        pipeline.remove(func)
        assert len(pipeline.functions) == 1
        del(pipeline)

        pipeline = DataPipeline(func, func, func, func)
        pipeline.remove(func, func, func)
        assert len(pipeline.functions) == 1
        del(pipeline)

    def test_clear(self):
        "Tests clearing the pipeline."
        pipeline = DataPipeline()
        pipeline.add(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = DataPipeline()
        pipeline.add(func)
        pipeline.add(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = DataPipeline(func, func)
        pipeline.add(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)

        pipeline = DataPipeline(func, func, func, func)
        pipeline.add(func, func)
        pipeline.remove(func)
        pipeline.clear()
        assert len(pipeline.functions) == 0
        del(pipeline)
