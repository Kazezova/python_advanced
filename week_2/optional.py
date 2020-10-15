from encode_decode import algorithm
key = 'а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш ы ю я'.split()
alpha = 'a b v g d e j z i y k l m n o p r s t u f h c 4 w y iu ya'.split()
optional = {key[j]: alpha[j] for j in range(len(key))}
inv_optional = {vl: ky for ky, vl in optional.items()}
text = input('text: ')
if text[0] in key:
    key = optional
else: 
    key = inv_optional
print(algorithm(key, text))
