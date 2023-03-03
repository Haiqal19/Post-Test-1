import random
import os
os.system ("cls")

def quick(ary):
    if len (ary) <=1:
        return ary
    else:
        pivot = ary[0]

        dakir = [x for x in ary [1:] if x <= pivot]
        dakan = [x for x in ary [1:] if x >= pivot]
        return quick(dakir) + [pivot] + quick(dakan)

isi_list = [0] * 10

for i in range (len(isi_list)):
    isi_list [i] = random.randint (1, 31)

print (f"List sebelum di sort : {isi_list}")

hs = quick (isi_list)
print (f"List setelah di sort : {hs}")