from collections import defaultdict
def groupanagrams(str):
    anagrams=defaultdict(list)
    for word in str:
        key=''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

# Example Walkthrough:

# Input: ["eat","tea","tan","ate","nat","bat"]

# "eat" → sorted = "aet" → {"aet": ["eat"]}

# "tea" → sorted = "aet" → {"aet": ["eat","tea"]}

# "tan" → sorted = "ant" → {"aet": [...], "ant": ["tan"]}

# "ate" → sorted = "aet" → {"aet": ["eat","tea","ate"], "ant":["tan"]}

# "nat" → sorted = "ant" → {"aet":[...], "ant":["tan","nat"]}

# "bat" → sorted = "abt" → {..., "abt":["bat"]}

# ✅ Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

# Complexity:
# Sorting each word: O(k log k)

# For n words: O(n × k log k)

# Space: O(n × k)

# 👉 Very common interview solution.


# optimal
def groupanagrams(str):
    anagrams=defaultdict(list)
    for word in str:

        count=[0]*26
    for char in word:
        count[ord(char)-ord('a')]+=1
        key=tuple(count)
        anagrams[key].append(word)
    return list(anagrams.values())
# Example Walkthrough:
# Input: ["eat","tea","tan","ate","nat","bat"]
# Word = "eat"

# counts = [1,0,0,...,1,...,1,...] (1 for 'a', 'e', 't')

# key = (1,0,0,...,1,...,1,...)

# Grouped with "tea", "ate" since they produce same key.

# Complexity:

# Counting characters: O(k) per word.

# For n words: O(n × k).

# Space: O(n × k).

# 👉 Faster than sorting, especially when words are long


 