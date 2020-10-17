from encode_decode import algorithm
latin = """
q w e r t y u i o p [ ] a s d f g h j k l ; ' z x c v b n m , . Q W E R T Y U I O P { } A S D F G H J K L : \" Z X C V B N M < > ? !
""".split()
cyril = """
й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю Й Ц У К Е Н Г Ш Щ З Х Ъ Ф Ы В А П Р О Л Д Ж Э Я Ч С М И Т Ь Б Ю ? !
""".split()
data = {latin[i]: cyril[i] for i in range(len(latin))}
inv_data = {v: k for k,v in data.items()}
text = input('text: ')
if text[0] in latin:
    key = data
else: 
    key = inv_data
print(algorithm(key, text))
