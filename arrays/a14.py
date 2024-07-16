class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        n=len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                left=j+1
                right=n-1
                while left<right:
                    tot=nums[i]+nums[j]+nums[left]+nums[right]
                    if tot>target:
                        right-=1
                    elif tot<target:
                        left+=1
                    else:
                        res.add(tuple(sorted((nums[i],nums[left],nums[right],nums[j]))))
                        left+=1
                        right-=1
        return res