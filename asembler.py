# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


instructions = ["MOV", "ADD", "SUB", "AND", "OR ", "NOT", "XOR", "SHL", "SHR", 
               "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", 
               "JLE", "JCR", "JOV"]

premade_instructions = {"MOV A,B":"0000000",
                        "MOV B,A":"0000001",
                        "ADD A,B":"0000100",
                        "ADD B,A":"0000101",
                        "SUB A,B":"0001000",
                        "SUB B,A":"0001001",
                        "AND A,B":"0001100",
                        "AND B,A":"0001101",
                        "OR A,B":"0010000",
                        "OR B,A":"0010001",
                        "NOT A,A":"0010100",
                        "NOT A,B":"0010101",
                        "NOT B,A":"0010110",
                        "NOT B,B":"0010111",
                        "XOR A,B":"0011000",
                        "XOR B,A":"0011001",
                        "SHL A,A":"0011100",
                        "SHL A,B":"0011101",
                        "SHL B,A":"0011110",
                        "SHL B,B":"0011111",
                        "SHR A,A":"0100000",
                        "SHR A,B":"0100001",
                        "SHR B,A":"0100010",
                        "SHR B,B":"0100011",
                        "INC B":"0100100",
                        "MOV A,(B)":"0101001",
                        "MOV B,(B)":"0101010",
                        "MOV (B),A":"0101011",
                        "ADD A,(B)":"0101110",
                        "SUB A,(B)":"0110010",
                        "AND A,(B)":"0110110",
                        "OR A,(B)":"0111010",
                        "NOT (B)":"0111110",
                        "XOR A,(B)":"1000001",
                        "SHL (B)":"1000101",
                        "SHR (B)":"1001000",
                        "INC (B)":"1001010",
                        "RST (B)":"1001100",
                        "CMP A,B":"1001101",
                        "CMP A,(B)":"1010010"}

lit_instructions = {"MOV A,dir":"0000010",#lit
                    "MOV B,dir":"0000011",#lit

                    "MOV A,(dir)":"0100101",#dir
                    "MOV B,(dir)":"0100110",#dir
                    "MOV (dir),A":"0100111",#dir
                    "MOV (dir),B":"0101000",#dir

                    "ADD A,dir":"0000110",#lit #nuevo
                    "ADD B,dir":"0000111",#lit #nuevo

                    "ADD A,(dir)":"0101100",#dir
                    "ADD B,(dir)":"0101101",#dir
                    "ADD (dir)":"0101111",#dir

                    "SUB A,dir":"0001010",#lit
                    "SUB B,dir":"0001011",#lit

                    "SUB A,(dir)":"0110000",#dir
                    "SUB B,(dir)":"0110001",#dir
                    "SUB (dir)":"0110011",#dir
                    
                    "AND A,dir":"0001110",#lit
                    "AND B,dir":"0001111",#lit

                    "AND A,(dir)":"0110100",#dir
                    "AND B,(dir)":"0110101",#dir
                    "AND (dir)":"0110111",#dir

                    "OR A,dir":"0010010",#lit
                    "OR B,dir":"0010011",#lit

                    "OR A,(dir)":"0111000",#dir
                    "OR B,(dir)":"0111001",#dir
                    "OR (dir)":"0111011",#dir
                    
                    "NOT (dir),A":"0111100",#dir
                    "NOT (dir),B":"0111101",#dir
                    
                    "XOR A,dir":"0011010",#lit
                    "XOR B,dir":"0011011",#lit

                    "XOR A,(dir)":"0111111",#dir
                    "XOR B,(dir)":"1000000",#dir
                    "XOR (dir)":"1000010",#dir primera pagina lista, segunda pagina lista hasta xor

                    ##falta arreglar los de aca a cambiarlos por dir y arreglar su opcode
                    "SHL (dir),A":"1000011",#dir
                    "SHL (dir),B":"1000100",#dir
                    
                    "SHR (dir),A":"1000110",#dir
                    "SHR (dir),B":"1000111",#dir
                    
                    "INC (dir)":"1001001",#dir
                    
                    "RST (dir)":"1001011",#dir
                    
                    "CMP A,dir":"1001110",#lit
                    "CMP B,dir":"1001111",#lit
                    
                    "CMP A,(dir)":"1010000",#dir
                    "CMP B,(dir)":"1010001",#dir

                    ##SALTOS
                    "JMP dir": "1010011",
                    "JEQ dir": "1010100",
                    "JNE dir": "1010101",
                    "JGT dir": "1010110",
                    "JLT dir": "1010111",
                    "JGE dir": "1011000",
                    "JLE dir": "1011001",
                    "JCR dir": "1011010",
                    "JOV dir": "1011011"}
##llamar a todos los casos de de dir o lit como dir
errors = []
asemb =  open("productoPunto.as")
outf = open("bin.out", "w")
numbers = "1234567890"
program = []
out = []
data = []


for line in asemb:
    program.append(line.strip())
i = 0



for line in program: 
    if line != "":
        line.strip().split(" ")
        data.append(line)
    else:
        break
data.pop(0)
print(data)
counter_mem = 0 
dta ={}
for i in data:
    if " " in i:
        i = i.split(" ")
        dta[i[0]] = "{0:08b}".format(counter_mem)
        counter_mem +=1
    else:
        dta[i] = "{0:08b}".format(counter_mem)
        counter_mem +=1

print(dta)



boolito = 0
for line in program:
    if line != "" and line[-1] != ":":
        if line == "CODE:":
            boolito = 1
        if boolito == 0:
            continue
        if not (line in premade_instructions):  
            variable = ""
            numero = ""
            for j in line: 
                if j in numbers:
                    numero += j
            print("{0:08b}".format(int(numero)))
            variable = line.replace(numero, "dir")
            if not (variable in lit_instructions):
                errors.append("Command Error, Line " + str(i) + ": '" + variable + "' is not a valid command")
            elif not (line[:3] in instructions):
                errors.append("Command Error, Line " + str(i) + ": '" + line + "' is not a valid command")
            else:
                if(variable in lit_instructions):
                    out.append(lit_instructions[variable] + "{0:08b}".format(int(numero)))
                
                else:
                    out.append(premade_instructions[variable] + "00000000")
                
            
        
            ####### Casos con "Lit" , solo sirve para reconocer casos, despues arreglamos para que lea bien el espacio #######
            ####### con una lista de todos los dir o lit que existan dentro de nuestro asemb
        
        i += 1
for error in errors:
    print(error)

for c in out:
    outf.write(c +"\n")


