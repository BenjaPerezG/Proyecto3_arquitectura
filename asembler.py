# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


instructions = ["MOV", "ADD", "SUB", "AND", "OR ", "NOT", "XOR", "SHL", "SHR", 
               "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", 
               "JLE", "JCR", "JOV","POP","PUSH", "RET", "CAL"]

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
                        "CMP A,(B)":"1010010",
                        "PUSH A": "0000010",
                        "PUSH B": "0000011",
                        "POP A" : "0100111",
                        "POP B" : "0101000",
                            }

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
                    "JOV dir": "1011011",
                    "CALL dir" : "1010011",
                    "RET" : "1010011"
                    }
##llamar a todos los casos de de dir o lit como dir
errors = []
asemb =  open("RadixSort.txt")
outf = open("bin.out", "w")
numbers = "1234567890"
program = []
out = []
data = []
lista_call = []
counter_stack = 255

for line in asemb:
    program.append(line.strip())
i = -1



for line in program: 
    if line != "":
        line.strip().split(" ")
        data.append(line)
    else:
        break
saltos = {}


data.pop(0)
largos = []
for l in data:
    largos.append(len(l))
largos.sort()
largos.reverse()
dataa =[]
c1 = 0
while c1 < len(largos) -1:
    for la in range(len(data)):
        if largos[c1] == len(data[la]):
            dataa.append(data[la])
            if c1 == len(largos) -1:
                break
            c1 +=1

counter_mem = 0 
dta ={}
for k in dataa:
    if " " in k:
        k = k.split(" ")
        dta[k[0]] = "{0:08b}".format(counter_mem)
        counter_mem +=1
    else: 
        dta[k] = "{0:08b}".format(counter_mem)
        counter_mem +=1



booolito = 0
contador = 0
salto = []
for  line in program:
    if line == "CODE:":
        booolito = 1
        continue
    if booolito == 0:
        continue
    if line != "":
        if line[-1] == ":":
            linea = line.replace(":", "")
            saltos[linea] = str(contador) 

            salto.append(linea)
        contador += 1


largos = []
for l in salto:
    largos.append(len(l))
largos.sort()
largos.reverse()
saltoo =[]
c1 = 0
while c1 < len(largos) -1:
    for la in range(len(salto)):
        if largos[c1] == len(salto[la]):
            saltoo.append(salto[la])
            if c1 == len(largos) -1:
                break
            c1 +=1

saltoss= { }
for e in saltoo:
    saltoss[e] = saltos[e] 



outt = []
boolito = 0
for line in program:
    i = i + 1
    if line == "CODE:":
        boolito = 1
    if boolito == 0:
        continue

    if line != "" and line[-1] != ":":
        if not (line in premade_instructions): 

            variable = ""
            numero = ""
            if "RET" in line:
                variable = line
                numero = lista_call[-1]
                lista_call.pop(-1)
            for s in saltoss:
                if s in line:
                    if "CALL" in line:
                        numero = saltoss[s]
                        variable1 = line.replace(s, "dir")
                        lista_call.append(i)
                        break
                    else:
                        numero = saltoss[s]
                        variable1 = line.replace(s, "dir")
                        break
            if numero == "":
                for dt in dta:    
                    if dt in line:
                        numero = dta[dt]
                        variable1 = line.replace(dt, "dir")
                        break
            if numero == "":
                        for j in line: 
                            if j in numbers:
                                numero += j
                        if numero != "":
                                variable1 = line.replace(numero, "dir")
                                
              
            if not (variable1 in lit_instructions):
                errors.append("Command Error, Line " + str(i) + ": '" + variable1 + "' is not a valid command")
            elif not (line[:3] in instructions):
                print(variable1)
                errors.append("Command Error, Line " + str(i) + ": '" + line + "' is not a valid command")
            else:
                if (variable1 in lit_instructions):
                    if numero != "":
                        out.append(lit_instructions[variable1] +"_" + "{0:08b}".format(int(numero)))
                        outt.append(variable1)
                    else:
                        numero = 0
                        out.append(lit_instructions[variable1] +"_" + "{0:08b}".format(int(numero)))
                        outt.append(variable1)
        else:
            if "PUSH" in line:
                out.append(premade_instructions[line] +"_" + "{0:08b}".format(int(counter_stack)))
                outt.append(line)
                counter_stack -=1
            elif "POP" in line:
                out.append(premade_instructions[line] +"_" + "{0:08b}".format(int(counter_stack)))
                counter_stack +=1
                outt.append(line)
            else:
                out.append(premade_instructions[line] + "_" + "00000000")
                outt.append(line)
                
            
        

for error in errors:
    print(error)

for c in out:
    outf.write(c +"\n")


