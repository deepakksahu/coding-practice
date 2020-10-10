#Subarray with given sum
#Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
#https://www.geeksforgeeks.org/find-subarray-with-given-sum/

# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Ouptut: Sum found between indexes 2 and 4
# Sum of elements between indices
# 2 and 4 is 20 + 3 + 10 = 33

# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Ouptut: Sum found between indexes 1 and 4
# Sum of elements between indices
# 1 and 4 is 4 + 0 + 0 + 3 = 7

# Input: arr[] = {1, 4}, sum = 0
# Output: No subarray found
# There is no subarray with 0 sum

def subarraySum(arr,n,sum):
    curr_sum=0
    for i in range(n):
        curr_sum=arr[i]
        j=i+1

        while j<=n:
            if curr_sum==sum:
                print("Found")
                output=[i,j-1]
                print(str(output))
                return 1
            if curr_sum > sum or j == n:
                break
            curr_sum=curr_sum+arr[j]
            j = j+1
    print("not found")
    return 0

subarraySum([1, 4, 20, 3, 10, 5],6,33)






