x = int(input("Valor -> "))

print(oct(x).replace("0o",""),"octal")
print(hex(x).replace("0x",""),"hexa")
print(bin(x).replace("0b",""),"binario")