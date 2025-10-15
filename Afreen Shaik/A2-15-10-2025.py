#reading last n lines
def last_n_lines(f, n):
    try:
        with open(f) as file:
            lines = file.readlines()
            for line in lines[-n:]:
                print(line, end='')
    except:
        print('File not found:', filename)
filename = 'sample.txt'
n = int(input("Enter the no of lines to read:"))
last_n_lines(filename, n)



#reading list line by line from file
filename = 'sample.txt'
try:
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        print(lines)
except FileNotFoundError:
    print('File not found:', filename)



#count no of lines in the given file
filename = 'sample.txt'
try:
    with open(filename,'r') as file:
        count = 0
        for line in file:
            count += 1
        print('Total number of lines:', count)
except FileNotFoundError:
    print('File not found:', filename)



#lengthy words in file
with open('sample.txt', 'r') as file:
    max_len = 0
    longest = ''
    for line in file:
        for word in line.strip().split(','):
            word = word.strip()
            if len(word) >= max_len:
                max_len = len(word)
                longest = word
print(max_len)
print(longest)