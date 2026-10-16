class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list) #provides default value for nonexistant key

        #array for all lower case characters to make accessing count indexes easier
        charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for word in strs:
            #array to represent characters in a string
            count = [0] * 26

            # map each word to a 'binary' type of array value , i.e. 0100405...0 would mean the word has 1b,4e's, and 5g's
            for char in word:
                index = charList.index(char)
                count[index]+=1
                
            # adds word to anagram group if 'binary' map exists in hashmap
            # convert array into tuple, meaning it cannot be changed, allowing for it to be used as a key (keys cannot be mutable)
            if tuple(count) in anagrams:
                anagrams[tuple(count)].append(word) 
            
            #uses 'binary' map value value as key for new hashmap element
            else:
                anagrams.update({tuple(count):[word]})

        return list(anagrams.values())