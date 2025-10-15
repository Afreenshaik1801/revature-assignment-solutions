# 5. Find the first occurrence of a number in a list using a while loop
nums_list = [4, 7, 2, 9, 7, 3]
search_num = 7
index = 0
found = False
while index < len(nums_list):
    if nums_list[index] == search_num:
        print(f"First occurrence of {search_num} is at index {index}")
        found = True
        break
    index += 1
if not found:
    print(f"{search_num} not found in the list")