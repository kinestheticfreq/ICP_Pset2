def findNumRepeats(X):
    if not X:
        return 0  # In case of an empty string

    repeats = {} 

    for char in X:
        if char in repeats.keys():
            repeats[char] += 1
        else:
            repeats[char] = 0
    sum = 0
    for key in repeats.keys():
        sum += repeats[key]
    return sum

# Example cases
print(findNumRepeats("blahbluh"))  # Output: 3
print(findNumRepeats("abcabcabd"))  # Output: 5

