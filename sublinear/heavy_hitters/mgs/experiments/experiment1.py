# Experiment 1 (Test)

from ..misra_gries_sketch import MisraGriesSketch

def test_mgs():
    
    mgs = MisraGriesSketch(10)  # Frequency threshold 10

    test1 = []

    for i in range(100):
        test1 += i * [f"word{i}"]

    mgs.process_stream(test1)

    frequencies = mgs.get_freq(test1)

    print(frequencies)