class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # k = number of outputs to return.  e.g. top k where k=2 means top 2 values
        # output an array that has all the numbers that fulfil the condition above

        #using hashmap to count integers
        count = {}

        # uses 'bucket sort' logic, at index 0 : store nothing, index 1: store list of values that appear once, index 2 : values that appear twice, etc
        # the number of times a value can appear is limited by the length of the array input
        results = [[] for i in range(len(nums) + 1)]

        #logic for counting updates
        # count[i] = 1 + count.get(i,0) better logically than the following code. .get() allows you to acces the value of a given key
        ## .get() method also allows you to return a value if the key does not exists , in the case of .get(i,0) will return 0 if i doesnt exist
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count.update({i:1})       

        # .items() returns dictionary KEY:VALUE pair
        # Syntax for looping through a dictionary requires 2 variables when looping through key:value pairs
        for i,val in count.items():
            results[val].append(i)

        print(results)
        # handles output formatting
        output = []
        # in range syntax = in range(start,end,traversal size)
        for j in range ((len(results)-1), 0, -1):
            for num in results[j]:
                output.append(num)
                # output only increments in size by 1, so this works
                if len(output) == k:
                    return output
                
       
