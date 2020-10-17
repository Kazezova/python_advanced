eng = sorted('qwertyuiopasdfghjklzxcvbnm'.upper())
def caesar(key, msg, k):
    ans = ''
    for i in msg:
        ans += key[(key.index(i) + k)%26]
        k += 1
    return ans 
def rot(key, rtr, shift_msg):
    rtr_ans = ''
    for i in shift_msg:
        rtr_ans += rtr[key.index(i)]
    return rtr_ans
def encode(enc_num, enc_eng, enc_rotors, enc_msg):
    enc_shift = caesar(enc_eng, enc_msg, enc_num)
    enc_v = enc_shift
    for i in range(3):
        enc_res = rot(enc_eng, enc_rotors[i], enc_v)
        enc_v = enc_res
    return enc_res
def decode(dec_num, dec_eng, dec_rotors, dec_msg):
    dec_v = dec_msg
    for i in range(2, -1, -1):
        dec_res = rot(dec_rotors[i], dec_eng, dec_v)
        dec_v = dec_res
    dec_eng.reverse()
    return caesar(dec_eng, dec_res, dec_num)
operation = input()
pseudo_random_number = int(input())
lst = []
for i in range(3):
    rotor = input()
    lst.append(rotor)
message = input()
if operation == 'encode':
    print(encode(pseudo_random_number, eng, lst, message))
else:
    print(decode(pseudo_random_number, eng, lst, message))