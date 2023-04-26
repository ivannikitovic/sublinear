from collections import Counter
import math
from sublinear.second_moment.ams.ams_sketch_2 import AMSSketch2

def test_ams_2():
    # Create a test stream
    test_stream = [i % 10 for i in range(10000)]

    # Initialize AMS Sketch 2
    epsilon = 0.1
    k = math.ceil(18 / epsilon)
    ams2 = AMSSketch2(len(test_stream), k)

    # Process the stream
    ams2.process_stream(test_stream)

    # Estimate the second moment
    estimated_second_moment_2 = ams2.get_estimate()

    print("Estimated second moment:", estimated_second_moment_2)

    # Compute the frequencies of unique elements in the stream
    element_frequencies = Counter(test_stream)

    # Calculate the actual second moment
    actual_second_moment = sum(freq ** 2 for freq in element_frequencies.values())

    print("Actual second moment:", actual_second_moment)
