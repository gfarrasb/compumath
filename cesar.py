clau=input("Digues la clau")
clau=int(clau)
text=input("Text a xifrar: ")
print("Xifrare " , text)
l=[]
for x in range(len(text)):
	b=ord(text[x])
	l.append(chr(b+clau))

xifrat = ''.join(l)
print(xifrat)





