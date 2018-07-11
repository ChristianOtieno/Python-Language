import collections
import string 

def caesar(text, shift):
    deque = collections.deque(string.ascii_lowercase)
    deque.rotate(-shift)
    deque = ''.join(list(deque))
    return text.translate(str.maketrans(string.ascii_lowercase.deque))

def viginere(text, key):
    text = [i for i in text]
    try:
        encrypted = [caesar(text[i], key[i]) for i in range(len(text))]
        return ''.join(encrypted)
    except IndexError:
        raise IndexError('Key is shorter than message')

deque = collections.deque(string.ascii_lowercase)
deque.rotate(1)
''.join(list(deque))

caesar('vigenere', 2)
