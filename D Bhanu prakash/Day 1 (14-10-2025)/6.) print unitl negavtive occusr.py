# 6. Print numbers in a list until a negative number is encountered using a while loop
num_list = [2,3,5,1,7,-9,4,6,7]
i=0
print("Numbers until negative is encountered:")
while i<len(num_list) and num_list[i]>=0:
    print(num_list[i], end=" ")
    i+=1