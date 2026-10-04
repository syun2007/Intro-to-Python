'''
Running code because rephactor doesn't show the output
Samuel Yun
Evil Rephactor
'''

my_string = "hello"

def count_vowels(string):
    counts = 0
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for i in string:
        if i == vowels:
            counts += 1
    return counts

print(count_vowels("amongus"))
