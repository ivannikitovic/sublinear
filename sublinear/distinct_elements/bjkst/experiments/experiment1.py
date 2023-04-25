# Experiment 1 (Test)

from ..bjkst_sketch import BJKSTSketch

def test_bjkst():

    n = 128
    b = 10
    c = 576
    epsilon = 0.1

    bjkst = BJKSTSketch(n, b, c, epsilon)

    test1 = []

    for i in range(100):
        test1 += i * [f"word{i}"]

    bjkst.process_stream(test1)

    estimate = bjkst.estimate_distinct_elements()

    print("Estimated number of distinct elements:", estimate)