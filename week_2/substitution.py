from encode_decode import algorithm
latin = "q w e r t y u i o p [ ] a s d f g h j k l ; ' z x c v b n m , .".split()
cyril = "й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю".split()
data = {latin[i]: cyril[i] for i in range(len(latin))}
inv_data = {v: k for k,v in data.items()}
text = input('text: ')
if text[0] in latin:
    key = data
else: 
    key = inv_data
print(algorithm(key, text))
