from ..morris_algorithm import MorrisCounter

def test_morris():
    morris = MorrisCounter()
    test_stream = [i for i in range(100)]

    morris.process_stream(test_stream)
    estimate = morris.estimate_count()

    print(f"Estimated count of elements: {estimate}")

    print(f"Actual count of elements: {len(test_stream)}")