def product_of_array_except_itself(arr):
    n=len(arr)
    prefix=1
    output=[1]*n
    for i in range(n):
        output[i]=prefix

        prefix=prefix*arr[i]
    suffix=1
    for i in range(n-1,-1,-1):
        output[i]*=suffix
        suffix*=arr[i]
    return output
# timecoplexity:O(n)
# spacecomplexityO(n)



