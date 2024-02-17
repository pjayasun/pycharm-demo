nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names=["Pranesh", "Gunner"]

print(nums)

print(nums[-1])

print(type(nums[-1]))

nums.append(200)

print(nums)

mil=[nums, names]

print(mil)

mil.clear()

print(mil)

nums.remove(2)

print(nums)

nums.pop(1)

print(nums)

nums.pop()
nums.pop()

del nums[3:]
print(nums)

nums.extend([10, 20, 30, 40, 50])
print(nums)

print(nums.count(10))
print(sum(nums))
print(max(nums))
print(min(nums))
