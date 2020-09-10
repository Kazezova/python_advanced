latin = "q w e r t y u i o p [ ] a s d f g h j k l ; ' z x c v b n m , .".split()
cyril = "й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю".split()
data = {latin[i]: cyril[i] for i in range(len(latin))}
inv_data = {v: k for k,v in data.items()}
key = 'а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш ы ю я'.split()
alpha =   'a b v g d e j z i y k l m n o p r s t u f h c 4 w y iu ya'.split()
optional = {key[j]: alpha[j] for j in range(len(key))}
inv_optional = {vl: ky for ky, vl in optional.items()}
def algorithm(db, string):
    result = ""
    txt = string.strip().split(" ")
    for each in txt:
        for letter in each:
            result += db[letter]
        result+=" "
    return result.strip()
text = input('text: ')
op = int(input('optional? 0 or 1 '))
if op == 1:
    if text[0] in key:
            key = optional
    else: 
        key = inv_optional
else:
    if text[0] in latin:
            key = data
    else: 
        key = inv_data
print(algorithm(key, text))
