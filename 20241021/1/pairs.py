import codecs


input_data = [x for x in input()]
# print(input_data)
st = ["".join((input_data[i].lower(), input_data[i + 1].lower()))
      for i in range(0, len(input_data) - 1) if (input_data[i].isalpha() and input_data[i + 1].isalpha())]
# print(st)
s = {pr for pr in st }
# print(s)
print(len(s))
