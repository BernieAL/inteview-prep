"""

"""

#MY BRUTE FORCE VERSION
def wordBreak(s,wordDict):

    def go(idx,currstr):

        if idx == len(s):
            return False
        
        if currstr in wordDict:
            return True
        
        return go(idx+1,currstr+s[idx])

    return go(0,"")

# wordDict = {'leet','code'}
# s = 'leetcode'
# print(wordBreak(s,wordDict))




def splitWord(s,wordDict):
    currstr = ""
    for i in range(len(s)):
        currstr+=s[i]
        print(currstr)
        
        for w in wordDict:
            if w in currstr:
                return True
            
    return False   

wordDict = {'leet','code'}
s = 'leetcode'
print(splitWord(s,wordDict))
