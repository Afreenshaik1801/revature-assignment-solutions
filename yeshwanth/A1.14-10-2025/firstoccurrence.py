numbers = [2, 3, 5, 7, 5, 9]
target = 5
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print("First occurrence at index:", index)
        break
    index += 1
