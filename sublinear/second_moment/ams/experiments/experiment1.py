from collections import Counter
from sublinear.second_moment.ams.ams_sketch_1 import AMSSketch1

def test_ams_1():
    # Create a test stream
    test_stream = [i % 10 for i in range(10000)]

    # Initialize AMS Sketch
    ams = AMSSketch1(n=len(test_stream))

    # Process the stream
    ams.process_stream(test_stream)

    # Estimate the second moment
    estimated_second_moment = ams.get_estimate()

    print("Estimated second moment:", estimated_second_moment)

    # Compute the frequencies of unique elements in the stream
    element_frequencies = Counter(test_stream)

    # Calculate the actual second moment
    actual_second_moment = sum(freq ** 2 for freq in element_frequencies.values())

    print("Actual second moment:", actual_second_moment)