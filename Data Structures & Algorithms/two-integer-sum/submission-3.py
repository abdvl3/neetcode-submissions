class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return index of two values that add to make targer number
        #return the answer with the smaller index first

        #checked dictionary used to store all numbers that have been 'checked' 
        checked = {}

        #enumerate method in python takes two input parameters (index,value) and uses the list to update them with the current index and current value
        for index,num in enumerate(nums):
            diff = target - num
            # checks if the number that needs to be added to reach the target (diff) exists in the dictionary. If it does, output. If not, add to dictionary.
            if diff in checked:
                return [checked[diff],index]
            else:
                # stores index as value and the number as key, as index is important thing that needs to be accessed
                checked.update({num:index})
                
