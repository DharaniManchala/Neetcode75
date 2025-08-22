def is_palindrome(str):
    left,right=0,len(str)-1
    while left<right:
        while left<right and not str[left].isalnum():
            left+=1
        while left<right and not str[right].isalnum():
            right-=1
        if str[left].lower()!=str[right].lower():
            return False
        left=left+1
        right=right-1
    return True
# timecompexity: O(n)
# spacecompexity: O(1)
