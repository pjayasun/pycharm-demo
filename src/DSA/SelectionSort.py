def sort(nums):
    n=len(nums)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if nums[j]<nums[min_index]:
                min_index=j
        nums[i], nums[min_index] = nums[min_index], nums[i]

        print(nums)

    return nums

nums = [6, 5, 4, 3, 19, 64, 72, 13, 2]
sort(nums)
print(nums)