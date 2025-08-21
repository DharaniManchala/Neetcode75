# naive approach
def longestconsecutive(nums):
    if not nums:
        return 0
    nums.sort()
    longest=1

    currentstreak=1
    n=len(nums)
    for i in range(1,n):
        if nums[i]==nums[i-1]+1:
            currentstreak+=1
        elif nums[i]!=nums[i-1]:
            currentstreak=1
        longest=max(longest,currentstreak)
    return longest
# timecompexity:O(nlogn)
# spacecmplexity:O(1)if inplacesorting
# optimal approach
def longestconsecutive(nums):
    numset=set(nums)
    longest=0
    for num in numset:
        if num-1 not in numset:
            length=1
            current=num
            while current+1 in numset:
                length+=1
                current+=1
            longest=max(longest,length)
    return longest
# timecomplexity:O(n)
# spacecomplexity:O(n)


