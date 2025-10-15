# 3. To Find the largest number in a list using a for loop
nums = [3, 9, 1, 6, 2, 8]
largest = nums[0]
for n in nums:
    if n>largest:
        largest=n
print("Largest number:", largest)