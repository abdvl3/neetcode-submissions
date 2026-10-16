class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        searched = set()
        for num in nums:
            if num in searched:
                return True
            else:
                searched.add(num)
        return False
