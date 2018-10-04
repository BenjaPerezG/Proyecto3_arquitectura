DATA:
inicio1
inicio2
n
i 0
j 0
v 0
pp 0

CODE:

assign:
MOV B,(inicio1)
MOV A,(B)
JEQ next
MOV B,(inicio2)
MOV B,(B)
JEQ next
MOV (j),B
MOV B,A


multiply:
ADD A,B
INC (i)
PUSH B
MOV B,(j)
CMP B,(i)
JGT next
POP B
JMP multiply

next:
ADD A,(pp)
MOV (pp),A
RST (i)
INC (v)
MOV B,(v)
CMP B,(n)
JGE end
INC (inicio1)
INC (inicio2)
JMP assign