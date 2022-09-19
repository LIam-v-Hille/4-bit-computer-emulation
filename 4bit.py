global ACC
global CIR
global OUT
global PRM
global PRO
global PC
ACC = 0b0000
CIR = 0b0000
PC = 0b0000
OUT = 0b0000



def instruction_set(instruction:bin, position:int):
    global ACC
    global CIR
    global OUT
    global PRM
    global PRO
    global PC
    '''
        0x0 - sta - start program
        0x1 - add - add the data of an address to ACC
        0x2 - sub - subtract the data of an address from ACC
        0x3 - mov - move the data of PRM_1 to PRM_2
        0x4 - lda - load the data of an address into ACC
        0x5 - wrt - write ACC to an address in PRM
        0x6 - out - write an address in PRM to OUT
        0x7 - jmp - jump to an address on PRO speciefied by CIR
        0x8 - ldc - load the data of an address into CIR
        ...
        0xF - stp - stop program
    '''
    i = instruction
    if i == 0b0000: # sta
        return position + 1
        

    elif i == 0b0001: # add
        ACC += PRM[PRO[PC+1]]
        print(f"ADD {PRM[PRO[PC+1]]}")
        return position + 2

    elif i == 0b0010: # sub
        ACC -= PRM[PRO[PC+1]]
        return position + 2

    elif i == 0b0100: # lda
        ACC = PRM[PRO[PC+1]]
        print(f"LDA {PRM[PRO[PC+1]]}")
        return position + 2

    elif i == 0b0101: # wrt
        PRM[PRO[PC+1]] = ACC
        print(f"WRT {ACC}")
        return position + 2

    elif i == 0b0110: # out
        OUT = PRM[PRO[PC+1]]
        print(f"OUT {PRM[PRO[PC+1]]}")
        return position + 2

    elif i == 0x07: # jmp
        print(f"JMP {CIR}")
        return CIR
    
    elif i == 0x08: # ldc
        CIR = PRM[PRO[PC+1]]
        print("LDC")
        return position + 2

    elif i == 0b1111: # stp
        print("STP")
        return -1

def run_program():
    global ACC
    global CIR
    global OUT
    global PRM
    global PRO
    global PC

    while 1:
        if PC == -1:
            print(OUT)
            break
        PC = instruction_set(PRO[PC],PC)
        #print(PC)



    

run_program()

