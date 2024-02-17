def sort(nums):
    n=len(nums)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

nums = [1, 2, 3, 4, 8, 6, 5, 4, 3, 2, 1]
sort(nums)
print(nums)