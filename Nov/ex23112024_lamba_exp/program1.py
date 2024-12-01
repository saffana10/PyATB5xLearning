# write a program to print the first non repeating char

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    else:
        return None

print(first_non_repeating("swiss"))
print(first_non_repeating("pepper"))
print(first_non_repeating("dada"))
