def is_isogram(string):
    if type(string) != str:
        raise TypeError('Argument should be a string')
    elif string == " ":
        return (string, False)
    else:
        for i in string:
            if string.count(i) > 1:
                return (string, False)
    return (string, True)
