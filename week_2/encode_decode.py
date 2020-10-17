def algorithm(db, string):
    result = ""
    txt = string.strip().split(" ")
    for each in txt:
        for letter in each:
            result += db[letter]
        result+=" "
    return result.strip()