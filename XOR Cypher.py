key=10001011
original=input("Put in the number you would like XOR incoded by the secret: ")
number=list(original)

def XOR1(i):
    if number[i] == "1":
        del number[i]
        number.insert(i, "0")
    else:
        del number[i]
        number.insert(i, "1")

def XOR2(i):
    if number[i] == "1":
        del number[i]
        number.insert(i, "1")
    else:
        del number[i]
        number.insert(i, "0")

i=7
XOR1(i)
i=6
XOR1(i)
i=5
XOR2(i)
i=4
XOR1(i)
i=3
XOR2(i)
i=2
XOR2(i)
i=1
XOR2(i)
i=0
XOR1(i)
joined = "".join(number)
print(joined)
encrypted=input("Put the sequence you would like to decrypt: ")
number=list(encrypted)

def XOR3(i):
    if number[i] == "0":
        del number[i]
        number.insert(i, "1")
    else:
        del number[i]
        number.insert(i, "0")

def XOR4(i):
    if number[i] == "1":
        del number[i]
        number.insert(i, "1")
    else:
        del number[i]
        number.insert(i, "0")
i=7
XOR3(i)
i=6
XOR3(i)
i=5
XOR4(i)
i=4
XOR3(i)
i=3
XOR4(i)
i=2
XOR4(i)
i=1
XOR4(i)
i=0
XOR3(i)
joined = "".join(number)
print(joined)
