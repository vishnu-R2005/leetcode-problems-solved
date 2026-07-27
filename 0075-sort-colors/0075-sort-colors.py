class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num]+=1
        index=0
        for _ in range(hash_map[0]):
            nums[index] =0
            index+=1
            
        for _ in range(hash_map[1]):
            nums[index] =1
            index+=1
            
        for _ in range(hash_map[2]):
            nums[index] =2
            index+=1
            
            
        






