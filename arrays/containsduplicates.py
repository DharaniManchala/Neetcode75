# Approach 1: Brute Force (Nested Loops)
# Logic:

# Compare every element with every other element.

# If any two elements are the same, return true.

# If no duplicates found after checking all, return false.

def contains_duplicates_bruteforce(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return True
    return False

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(contains_duplicates_bruteforce(arr))  # Output: False

    arr_with_duplicates = [1, 2, 3, 4, 5, 3]
    print(contains_duplicates_bruteforce(arr_with_duplicates))  # Output: True

#     Time: O(n²) (because of nested loops)

# Space: O(1) (no extra memory)

# ✔ Works, but very slow for large arrays.

# sorting the array and checking adjacent elements
def contain_duplicates_sorting(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i]==arr[i+1]:
            return True
    return False
# Complexity:

# Time: O(n log n) (for sorting)

# Space: O(1) or O(log n) (depending on sorting algorithm)

# ✔ Faster than brute force, but still not the best.

# using hashmap
def contains_duplicates_hashmap(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
# Complexity:

# Time: O(n) (because set operations are O(1) average case)

# Space: O(n) (to store elements in set)

# ✔ Best approach for large arrays.
    