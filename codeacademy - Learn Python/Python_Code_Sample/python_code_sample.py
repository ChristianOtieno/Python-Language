pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]


pantry_counts {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
        pass
    else:
        pantry_counts[item] = 1
        pass
    pass
    