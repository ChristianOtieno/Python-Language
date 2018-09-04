def is_isogram(word):
    return (word, True) if word and len(set(word)) == len(word) else (word, False)
is_isogram('assess') 
is_isogram('rhyme')  
