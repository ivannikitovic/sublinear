from ...bjkst.bjkst_sketch import BJKSTSketch
from ..sketch_switch import SketchSwitch


def test_adv_robust_1():
    epsilon = 0.1
    delta = 0.1
    n = 128
    m = 2

    test1 = []

    for i in range(100):
        test1 += i * [f"word{i}"]

    insertion_only_de = SketchSwitch(BJKSTSketch, epsilon, delta, m, n)
    insertion_only_de.process_stream(test1)
    estimate = insertion_only_de.get_estimate()

    print("Estimated number of distinct elements:", estimate)