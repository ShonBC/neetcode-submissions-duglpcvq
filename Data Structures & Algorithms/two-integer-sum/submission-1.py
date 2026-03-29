class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i in range(len(nums)):
            print(pair, nums[i])
            if target - nums[i] not in pair:
                pair[nums[i]] = i
            else:
                break
        return [pair[target - nums[i]], i]