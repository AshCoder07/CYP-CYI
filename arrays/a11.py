class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n):
            nums[abs(nums[i])-1]*=-1
            if nums[abs(nums[i])-1]>0:
                res.append(abs(nums[i]))
        return res