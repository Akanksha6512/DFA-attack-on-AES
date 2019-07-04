
from akank_math import *

unknst = 0x00 >> 120 ## Initialize penultimate state with 0
u = to_matrix(unknst)


c = int(raw_input("Enter correct cipher: "),16)
ct = int(raw_input("Enter fault cipher1: "),16)
cs = int(raw_input("Enter fault cipher2: "),16)

f1 = int(raw_input("Enter fault1: "),16)
f2 = int(raw_input("Enter fault2: "),16)

x = c ^ ct
y = to_matrix(x)

a = c ^ cs
b =to_matrix(a)
#print printmatrix(to_matrix(x))

for p in range(0,16):
    tmp = y[p % 4][p / 4]
    tmp1 = b[p % 4][p / 4]
    for i in sbox:
        for j in sbox:
            if(i^j == tmp):
                for k in sbox:
                    if(i ^ k == tmp1):
                        s1 = int(i)
                        s2 = int(j)
                        s3 = int(k)
                        s11 = inv_sbox[s1]
                        s22 = inv_sbox[s2]
                        s33 = inv_sbox[s3]

                        if((s22 ^ f1)==s11):
                            if((s33 ^ f2) == s11):
                                u[p % 4][p / 4] = s11
u = inv_shiftrows(u)
#print printmatrix(u)
unknst = to_bitstring(shiftrows(subbytes(u)))
fnkey = to_matrix(c ^ unknst)
print "\nROUND KEYS\n"
print printmatrix(fnkey)

lkey = fnkey
m = 10

for r in range(0,10):
    
    rkey = to_matrix(0x00 >> 120)
    

    for i in range(4,16):
        j = i-4
        rkey[i % 4][i / 4] = lkey[j%4][j/4] ^ lkey[i%4][i/4]   ### from byte 4-15 can be replaced by xor two columns

    rkey[3][0] = rkey[0][3]         #### One byte reverse row shift
    l=0

    for i in range(13,16):
        rkey[l%4][l/4]=rkey[i%4][i/4]
        l+=1

    for i in range(0,4):
        j = int(rkey[i%4][i/4])
        rkey[i%4][i/4]=sbox[j]

    rconkey = to_matrix(rcon[m] << 120)

    for i in range(0,4):
        rkey[i%4][i/4] = rkey[i%4][i/4] ^ rconkey[i%4][i/4] ^ lkey[i%4][i/4]

    print printmatrix(rkey)

    lkey = rkey
    m-=1

print "ORIGINAL AES KEY HACKED!!! ----> "+hex(to_bitstring(rkey))


