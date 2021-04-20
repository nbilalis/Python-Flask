# 'The Life of Brian' -> print vertically


def word(string):
    words = string.split(' ')
    print(words)
    for word in words:
        print(word, end='\n')


word('The Life of Brian')
