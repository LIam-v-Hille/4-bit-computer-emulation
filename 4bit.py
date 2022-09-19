global ACC
global CIR
global OUT
global PRM
global PRO
global PRC
ACC = 0b0000
CIR = 0b0000
PRC = 0b0000
OUT = 0b0000
# write your own program here or copy one from programs.txt
PRM = [0xA, 0x1, 0x1, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
PRO = [0x4,0x0,0x6, 0x0, 0xC, 0xA, 0x3,0x5, 0x2 ,0xB, 0x2, 0xF, 0x4, 0x0, 0x2, 0x1, 0x5, 0x0, 0x7]

def instruction_set(instruction:bin, position:int, verbose:bool):
    global ACC
    global CIR
    global OUT
    global PRM
    global PRO
    global PRC
    '''
        0x0 - div - divide ACC by the data of an address
        0x1 - add - add the data of an address to ACC
        0x2 - sub - subtract the data of an address from ACC
        0x3 - mov - move the data of PRM_1 to PRM_2
        0x4 - lda - load the data of an address into ACC
        0x5 - wrt - write ACC to an address in PRM
        0x6 - out - write an address in PRM to OUT
        0x7 - jmp - jump to an address on PRO speciefied by CIR
        0x8 - ldc - load the data of an address into CIR
        0x9 - mlt - multiply the ACC by the data of an address
        0xA - cmp - compare the data of an address with the data of ACC
        0xB - ift - execute the instruction 2 infront of it if the address 1 infront of it is >=1
        0xC - wro - print the OUT register

        0xF - stp - stop program and print OUT
    '''
    i = instruction
    if i == 0b0000: # div
        ACC /= PRM[PRO[PRC+1]]
        if verbose: print(f"DIV {PRM[PRO[PRC+1]]}")
        return position + 2
        

    elif i == 0b0001: # add
        ACC += PRM[PRO[PRC+1]]
        if verbose: print(f"ADD {PRM[PRO[PRC+1]]}")
        return position + 2

    elif i == 0b0010: # sub
        ACC -= PRM[PRO[PRC+1]]
        if verbose: print(f"SUB {PRM[PRO[PRC+1]]}")
        return position + 2

    elif i == 0b0100: # lda
        ACC = PRM[PRO[PRC+1]]
        if verbose: print(f"LDA {PRM[PRO[PRC+1]]}")
        return position + 2

    elif i == 0b0101: # wrt
        PRM[PRO[PRC+1]] = ACC
        if verbose: print(f"WRT {PRM[PRO[PRC+1]]}")
        return position + 2

    elif i == 0b0110: # out
        OUT = PRM[PRO[PRC+1]]
        if verbose: print(f"OUT {PRM[PRO[PRC+1]]}")
        return position + 2

    elif i == 0x07: # jmp
        if verbose: print(f"JMP {CIR}")
        return CIR
    
    elif i == 0x08: # ldc
        CIR = PRM[PRO[PRC+1]]
        if verbose: print(f"LDC {PRM[PRO[PRC+1]]}")
        return position + 2
    
    elif i == 0x09: # mlt
        ACC *= PRM[PRO[PRC+1]]
        if verbose: print(f"MLT {PRM[PRO[PRC+1]]}")
        return position + 2

    elif i == 0xA: # cmp
        if PRM[PRO[PRC+1]] == ACC:
            ACC = 1
        else:
            ACC = 0
        if verbose: print(f"CMP {PRM[PRO[PRC+1]]} {ACC == 1}")
        return position + 2

    elif i == 0xB: # ift
        if PRM[PRO[PRC+1]]:
            if verbose: print(f"IFT {PRM[PRO[PRC+1]]} TRUE")
            return position + 2
        else:
            if verbose: print(f"IFT {PRM[PRO[PRC+1]]} FALSE")
            return position + 3

    elif i == 0xC: # wro
        print(OUT)
        return position + 1

    elif i == 0b1111: # stp
        if verbose: print("STP")
        return -1

def run_program(verbose:bool):
    global ACC
    global CIR
    global OUT
    global PRM
    global PRO
    global PRC

    while 1:
        if PRC == -1:
            print(OUT)
            break
        PRC = instruction_set(PRO[PRC],PRC, verbose)
        #print(PC)



    

run_program(False)

