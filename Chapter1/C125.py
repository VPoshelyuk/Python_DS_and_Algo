def remove(word):
    punc = ['.', ',', '!', '?', ':', ';', '-']
    new_word = ''
    for i in word:
        if i not in punc: new_word += i
    return new_word

print(remove('apple?'))
print(remove('hd,a:sie,w-n,fe;dw!!!'))
