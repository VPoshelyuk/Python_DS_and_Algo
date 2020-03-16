def voweslCounter(word):
    l_word = word.lower()
    vowels = ['a','e','i','o','u']
    count = 0
    for char in l_word:
        if char in vowels: count+=1
    return count

print(voweslCounter('apple'))
print(voweslCounter('hdasiewnfedw'))