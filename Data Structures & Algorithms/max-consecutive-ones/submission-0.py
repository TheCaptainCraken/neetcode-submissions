class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maximum = 0

        for n in nums:
            if n == 1:
                counter += 1
                maximum = max(counter, maximum)
            else:
                counter = 0

        return maximum 


