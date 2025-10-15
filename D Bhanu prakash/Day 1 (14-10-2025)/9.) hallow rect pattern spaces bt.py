# 9. Draw pattern 2
rows = 5
print("Pattern 2:")
for i in range(1, rows + 1):
    if i==1 or i==rows:
        print("* " * rows)
    else:
        print("*" + " " * (2*(rows-2)+1) + "*")