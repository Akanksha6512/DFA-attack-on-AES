from aes import *

plain = int(raw_input("\nEnter plaintext: "),16)
inj_key = int(raw_input("\nEnter Key: "),16)

flt1 = int(raw_input("\nEnter fault1 to be injected: "),16)
flt2 = int(raw_input("\nEnter fault2 to be injected: "),16)

ct1 = encrypt(plain,inj_key)
ct2 = encrypt(plain,inj_key,fault=flt1,floc=12)
ct3 = encrypt(plain,inj_key,fault=flt2,floc=12)

print "\nCORRECT CIPHER: "+hex(ct1)
print "\nFAULT CIPHER 1: "+hex(ct2)
print "\nFAULT CIPHER 2: "+hex(ct3)+"\n"
