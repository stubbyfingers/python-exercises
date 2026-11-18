from dis import dis #This function stands for "disassemble" to show the simpler instructions the computer runs ("byte code" or "assemble language")
# print(dis("while True: x = 10"))

print(dis('''
x = 1
if x > 0:
    y = 10
'''))