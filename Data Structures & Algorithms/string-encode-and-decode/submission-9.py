class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word)) + '#' +  word
        print (res) 
        return res
        
                
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = ""
                while s[i] != '#':
                    num = num + s[i]
                    i +=1
                i+=1 
                length = int(num)
                print(length)
                res.append(s[i:i+length])
                i += length
        return res
            

            
