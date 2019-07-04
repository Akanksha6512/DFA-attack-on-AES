"""inp = '0x00000100000000000000111111111111aaaaaaaaaaaaaaaa'
s1 = inp[0:34]"""

inp='0xf0f0'
s1=inp[0:4]
print s1
x = int(s1,16)
y = hex(x)
print x
print y
#z = y
z = '0xff'
p = 18
print type(p)
ph = str(hex(p))
print ph
print p & p
print z
print type(z)
print type(y)
print x & x
#print int(str(y),16)
