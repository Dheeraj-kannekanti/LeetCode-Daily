class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left,right = 0 , len(nums)-1
        nums.sort()
        pair_count = 0
        while left<right:
            current_sum = nums[left]+nums[right]
            if current_sum == k:
                left+=1
                right-=1
                pair_count+=1
            elif current_sum<k:
                left+=1
            else:
                right-=1
        return pair_count

        