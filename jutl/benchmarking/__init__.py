# Import submodule files so
# classes and functions are usable at
# 'from jutl.benchmarking import _' level.
from .latency import *

# Only show functions specified in
# submodule files to the outside world.
__all__ = latency.__all__


# Benchmarks:
# - Timed function call: Latency

# - Generic benchmamrk class: Benckmark
# - Timed pipeline with single data input (InstructionPipeline): Benchmark
# - Timed pipeline with multiple data inputs & flippable loops (DataPipeline): 


