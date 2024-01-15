dec = 65
octal = 0o101 #8진수로 쓰고싶으면 0o
hexadecimal = 0x41 #16진수로 쓰고싶으면 0x
binary = 0b01000001 #이진수로 쓰고싶으면 0b
print(dec,octal,hexadecimal,binary) #print 시 10진수로 변환하여 출력됨 (출력결과 65 65 65 65)
print(chr(dec), chr(octal), chr(hexadecimal), chr(binary)) #A
print(bin(dec), bin(octal), bin(hexadecimal), bin(binary)) #0b1000001
print(ord('B'), ord('Z'), ord('a'), ord('2')) #66, 90, 97, 50
