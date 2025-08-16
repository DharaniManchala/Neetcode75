# bruteforce
def twosum(arr,target):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
# Complexity:

# Time: O(n²)

# Space: O(1)

# 👉 Works, but too slow for large array

# hashing
def twosum(arr,target):
    seen={}
    for i,num in enumerate(arr):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
# Complexity:
# Time: O(n) (each lookup in hashmap is O(1) on average)

# Space: O(n) (storing up to n elements in dictionary)

# 👉 This is the best solution used in interviews.