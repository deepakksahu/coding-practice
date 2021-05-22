def majorityElement(nums) -> int:
    dic = {}
    for i, num in enumerate(nums):
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
        if dic[num] > (len(nums) / 2):
            return num
    return -1

print(majorityElement([3,3,3,3,2,2,2,2,2,3]))