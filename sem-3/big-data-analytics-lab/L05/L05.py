import heapq as heapq
from collections import defaultdict, deque


class DataStream:
    def __init__(self, k):
        self.data_queue = deque()
        self.k_min_heap = []
        self.k_max_heap = []
        self.element_counts = defaultdict(int)
        self.k = k

    def add_data_point(self, data_point):
        # Update frequency moments
        self.element_counts[data_point] += 1

        # Update K-minimum and K-maximum heaps
        self.update_k_heaps(data_point)

    def update_k_heaps(self, data_point):
        # Update K-minimum heap
        heapq.heappush(self.k_min_heap, data_point)
        if len(self.k_min_heap) > self.k:
            heapq.heappop(self.k_min_heap)

        # Update K-maximum heap
        heapq.heappush(self.k_max_heap, -data_point)
        if len(self.k_max_heap) > self.k:
            heapq.heappop(self.k_max_heap)

    def get_k_min_values(self):
        return sorted(self.k_min_heap)

    def get_k_max_values(self):
        return sorted([-x for x in self.k_max_heap])

    def get_frequency_moments(self):
        # Calculate first, second, and third frequency moments
        f0 = len(self.element_counts)
        f1 = sum(self.element_counts.values())
        f2 = sum(count**2 for count in self.element_counts.values())
        f3 = sum(count**3 for count in self.element_counts.values())

        return f0, f1, f2, f3


# Example Usage:
k = 3  # Choose the value of K
data_stream = DataStream(k)

# Simulate data streaming
data_points = [4, 2, 7, 1, 9, 8, 5, 2, 4, 7, 1]
for point in data_points:
    data_stream.add_data_point(point)

# Get frequency moments, K-minimum, and K-maximum values
f0, f1, f2, f3 = data_stream.get_frequency_moments()
k_min_values = data_stream.get_k_min_values()
k_max_values = data_stream.get_k_max_values()

print(f"Zeroth Frequency Moment (F_0): {f0}")
print(f"First Frequency Moment (F_1): {f1}")
print(f"Second Frequency Moment (F_2): {f2}")
print(f"Third Frequency Moment (F_3): {f3}")
print(f"K-Minimum Values: {k_min_values}")
print(f"K-Maximum Values: {k_max_values}")
