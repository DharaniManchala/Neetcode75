from collections import Counter
def top_k_elements(arr,k):
    freq=Counter(arr)
    sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)

    result= [item[0] for item in sorted_freq[:k]]
    return result

# Time Complexity:

# Counting frequencies: O(n)

# Sorting: O(n log n)

# Final slicing: O(k)
# ➡️ Overall: O(n log n)

# Space: O(n) — for the frequency map.

# by using heAP STRUCTURE
import heapq
from collections import Counter
def top_k_elements(arr,k):
    freq=Counter(arr)
    heap=[(-count,num)for num,count in freq.items()]
    heapq.heapify(heap)
    result=[]
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
# Time Complexity:
# Sorting approach → O(n log n)

# Heap approach → O(n log k) (faster when k is much smaller than n)

# bucket sort approach
from collections import Counter
def top_k_elements(arr,k):
    freq=Counter(arr)
    bucket=[[] for _ in range(len(arr)+1)]
    for num,count in freq.items():
        bucket[count].append(num)
    result=[]
    for i in range(len(bucket)-1,0,-1):
        for num in bucket[i]:
            result.append(num)
            if len(result)==k:
                return result
            
            # Complexity

# Time: O(n)

# Counting frequencies = O(n)

# Filling buckets = O(n)

# Traversing buckets = O(n)

# Space: O(n) (buckets)

