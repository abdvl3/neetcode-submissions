class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        for x,num in enumerate (nums):
            if num in appeared.values():
                return True
            else:
                appeared[x] = num
        return False