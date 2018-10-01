DATA:
inicio1
inicio2
n
i 0
j 0
pp 0

CODE:

assign:
MOV B,(inicio1)
MOV A,(B)
MOV B,(inicio2)
MOV B,(B)
MOV (j),B
MOV A,B

multiply:
ADD A,B
INC (i)
PUSH B
MOV B,(j)
CMP B,(i)
JGT next
POP B
INC (i)
JMP multiply

next:
ADD A,(pp)
MOV (pp),A
RST (i)
INC (j)
MOV B,(j)
CMP B,(n)
JGE end
INC (inicio1)
INC (inicio2)
JMP assign