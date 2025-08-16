# sorting
def is_anagram_sorting(s1,s2):
    return sorted(s1)==sorted(s2)
# complexities
# Complexity:

# Time: O(n log n) (because of sorting)

# Space: O(1) or O(n) depending on sort implementation
# hashmap with two dixtonARIES
def is_anagram_hashmap(s1,s2):
    if len(s1)!=len(s2):
        return False
    count1={}
    count2={}
    for char in s1:
        count1[char]=count1.get(char,0)+1
    for char in s2:
        count2[char]=count2.get(char,0)+1
    return count1==count2
# Time: O(n) (just one pass through each string)

# Space: O(1) (since only 26 lowercase letters if restricted to English alphabets, otherwise O(n) in general)
  
#   hashing using a single dictonary
def is_anagram_single_hashmap(s1,s2):
    if len(s1)!=len(s2):
        return False
    count={}
    for char in s1:
        count[char]=count.get(char,0)+1
    for char in s2:
        count[char]=count.get(char,0)-1
    for val in count.values():
        if val!=0:
            return False
    return True
# Time: O(n) (just one pass through each string)
# Space: O(1) (since only 26 lowercase letters if restricted to English alphabets, otherwise O(n) in general)


        

        