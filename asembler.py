# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

instructions = ["MOV", "ADD", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", 
               "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", 
               "JLE", "JCR", "JOV"]

premade_instructions = {"MOV A,B":0000000,
                        "MOV B,A":0000001,
                        "ADD A,B":0000100,
                        "ADD B,A":0000101,
                        "SUB A,B":0001000,
                        "SUB B,A":0001001,
                        "AND A,B":0001100,
                        "AND B,A":0001101,
                        "OR A,B":0010000,
                        "OR B,A":0010001,
                        "NOT A,A":0010100,
                        "NOT A,B":0010101,
                        "NOT B,A":0010110,
                        "NOT B,B":0010111,
                        "XOR A,B":0011000,
                        "XOR B,A":0011001,
                        "SHL A,A":0011100,
                        "SHL A,B":0011101,
                        "SHL B,A":0011110,
                        "SHL B,B":0011111,
                        "SHR A,A":0100000,
                        "SHR A,B":0100001,
                        "SHR B,A":0100010,
                        "SHR B,B":0100011,
                        "INC B":0100100,
                        "MOV A,(B)":0101001,
                        "MOV B,(B)":0101010,
                        "MOV (B),A":0101011,
                        "ADD A,(B)":0101110,
                        "SUB A,(B)":0110010,
                        "AND A,(B)":0110110,
                        "OR A,(B)":0111010,
                        "NOT (B)":0111110,
                        "XOR A,(B)":1000001,
                        "SHL (B)":1000101,
                        "SHR (B)":1001000,
                        "INC (B)":1001010,
                        "RST (B)":1001100,
                        "CMP A,B":1001101,
                        "CMP A,(B)":1010010}

errors = []
asemb = open("main.as")
out = open("bin.out", "w")

program = []

for line in asemb:
    program.append(line.strip().split())
i = 0
for line in program:
    if not (line[0] in instructions):
        errors.append("Command Error, Line " + str(i) + ": '" + line[0] + "' is not a valid command")
    i += 1

for error in errors:
    print(error)

