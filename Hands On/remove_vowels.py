def remove_vowles(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        string = string.replace(vowel, '')
    return string

print(remove_vowles("neha"))