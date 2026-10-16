class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #use a hashmap
        sorted = {}
        for n,i in enumerate(nums):
            if i in sorted.values():
                return True
            else:
                sorted.update({n:i})
        return False
        