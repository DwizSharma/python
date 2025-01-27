def count_vowel(s):
    count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            count += 1
    return count
s = input("Enter the string : ")
print("Number of vowels in the string are : ",count_vowel(s))