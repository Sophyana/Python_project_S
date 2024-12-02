# code - encode
"""
print("бМХЛЮМХЕ".encode("KOI8-R").decode("1251"))
print("ОХРЮМХЕ".encode("KOI8-R").decode("1251"))
"""

# сериализация

import pickle

"""
with open("binary_file", "rb") as f:
    data = pickle.load(f)"""

"""
class SecCls:
    def __init__(self, lst, dct, num, str):
        self.lst =  lst
        self.dct = dct
        self.num = num
        self.str  = str


ser = SecCls([1, 2, 3], {4, 5, 6}, 100, "qwert")
with open("ser_as_file", "wb") as f:
    pickle.dump(ser, f)
    res = pickle.dumps(ser)

del ser

ser1 = pickle.loads(res)
print(ser1.num)
"""

# typical binary files

import struct

with open("binary_file_new", "a+b") as f:
    res = struct.pack("=f3si", 0.1, bytes([1,2,3]), 11 )
    f.write(res)
    res = struct.pack("=f3si", 0.2, bytes([2,3,4]), 12 )
    f.write(res)
    res = struct.pack("=f3si", 0.3, bytes([3,4,5]), 13 )
    f.write(res)



"""import binascii

binascii.hexlify(Bytes, ' '))"""


with open("binary_file_new", "rb") as file:
    record = file.read(struct.calcsize("!f3si"))
    res = struct.unpack("!f3sirecord")



# (0.1, [1,2,3], 11); (0.2, [2,3,4], 12); (0.3, [3,4,5], 13)