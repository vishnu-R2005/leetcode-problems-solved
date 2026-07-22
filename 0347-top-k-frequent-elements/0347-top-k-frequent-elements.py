class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}

        for num in nums:
            fre[num] = fre.get(num, 0) + 1

        sorted_list = list(fre.items())
        sorted_list.sort(key=lambda x: x[1], reverse=True)

        return [x[0] for x in sorted_list[:k]]