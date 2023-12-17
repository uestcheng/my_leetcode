class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # result_dict
        rd = {}
        for i in range(n):
            res = target - nums[i]
            if res in rd:
                return [rd[res], i]
            rd[nums[i]] = i 
        return []