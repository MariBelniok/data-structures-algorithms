def getSumAbsoluteDifferences(nums):
    ans = []
    index = 0
    while len(ans) != len(nums):
        value = 0
        for i in range(0, len(nums)):
            value += abs(nums[index] - nums[i])
        ans.append(value)
        index += 1
    return ans  

getSumAbsoluteDifferences([2, 3, 5])