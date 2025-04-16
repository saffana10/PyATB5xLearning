#write a program to print the frequency of each character in a string
# e.g string = automation

# step1 : I/p and 0/p
string = input("Enter the input e.g. automation\n")

char_count ={}

for char in string:
    char_count[char] = char_count.get(char,0)+1

print(char_count)