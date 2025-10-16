
#read last n lines
with open('nutrient.txt','r') as file:
    n = int(input("Enter the no of lines:"))
    lines = file.readlines()
    for line in lines[len(lines) - n:]:
        print(line.strip())


#create a list by reading line by line
with open('nutrient.txt','r') as file:
    lines = file.readlines()
    ls = []
    for line in lines:
        ls.append(line.strip())
    print(ls)


#count not of lines in a file
with open('nutrient.txt','r') as file:
    lines = file.readlines()
    print(len(lines))


#largest word in list
with open('nutrient.txt','r') as file:
    lines = file.readlines()
    max_len = 0
    longest = ''
    for line in lines:
        words = line.split(',')
        for word in words:
            if len(word) >= max_len:
                max_len = len(word)
                longest = word
    print(max_len)
    print(longest)