class codec:
    def encode(self,strs):
        encoded=""
        for word in strs:
            encoded+=str(len(word))+"#"+word
        return encoded
    def decode(self,s):
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            word=s[i:i+length]
            result.append(word)
            i+=length
        return result
# ✅ Final Answer

# Encoding

# Time: O(L) (if optimized with join) or O(n·L) with repeated concatenation.

# Space: O(L)

# Decoding

# Time: O(L)

# Space: O(L)

    
