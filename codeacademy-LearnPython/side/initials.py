name = str(input("Name: "))
initials = ""
for c in name:
    if c.isupper():
        initials += c
print(initials)