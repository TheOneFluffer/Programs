def ziplist(nums, n):
    #Insert your codes here
    numlist = []
    index1 = 0
    index2 = n + index1
    while index2 != len(nums):
        numlist.append(nums[index1])
        numlist.append(nums[index2])
        index1 += 1
        index2 = n + index1
    return numlist



nums = [10, 3, 7, 5, 2, 13] #x1 x2 x3 y1 y2 y3
n = 2
print(ziplist(nums, n)) #x1 y1 x2 y2 x3 y3