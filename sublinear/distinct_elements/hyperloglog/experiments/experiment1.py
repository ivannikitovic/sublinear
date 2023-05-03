from ..hyper_log_log import HyperLogLog

def test_hll():
    hll = HyperLogLog(16) # Initialize HyperLogLog with 16-bit bucket address
    
    test2 = []
    for i in range(1000):
        test2 += i * [f"word{i}"]

    for item in test2:
        hll.add(item)

    cardinality = hll.estimate_cardinality()
    print(f"Estimated number of distinct elements: {cardinality}")