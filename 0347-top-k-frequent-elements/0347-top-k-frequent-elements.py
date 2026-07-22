class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Traverse from highest frequency to lowest
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result