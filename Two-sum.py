class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = [0 , 0]
        for i in range (0, len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ls[0] = i
                    ls[1] = j
                    break

        return ls
