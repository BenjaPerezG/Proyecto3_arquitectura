# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

instructions = ["MOV", "ADD", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", 
               "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", 
               "JLE", "JCR", "JOV"]
               
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

