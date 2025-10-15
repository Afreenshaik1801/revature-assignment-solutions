# 7. Print numbers from 1 to 10. If a number is even, break the loop using a for loop and else clause
print("Numbers from 1 to 10 (break on even):")
for i in range(1, 11):
    if i%2==0:
        print(f"Even number {i} found, I am breaking the loop guys")
        break
    print(i)
else:
    print("No even number found")