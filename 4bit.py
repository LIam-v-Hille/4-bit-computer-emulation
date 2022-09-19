global ACC
global CIR
global OUT
global PRM
global PRO
global PC
ACC = 0b0000
CIR = 0b0000
PC = 0b0001
OUT = 0b0000
PRM = [0b0001, 0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000] # 4-bit RAM, 4-bit ADDRS BUS
PRO = [0b0000, 0b0100, 0b0000, 0b0001, 0b0001, 0b0101, 0b0010, 0b0110, 0b0010, 0b1111, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000] # program

def instruction_set(instruction:bin, next_instruction:bin, position:int):
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
        ...
        0xF - stp - stop program
    '''
    i = instruction
    inp = next_instruction
    if i == 0b0000: # sta
        PC = 0b0000 # start listening
        pass

    elif i == 0b0001: # add
        ACC += PRM[inp]
        return 0b0010

    elif i == 0b0010: # sub
        ACC -= PRM[inp]
        return 0b0010

    elif i == 0b0100: # lda
        ACC = PRM[inp]
        return 0b0010

    elif i == 0b0101: # wrt
        PRM[inp] = ACC
        return 0b0010

    elif i == 0b0110: # out
        OUT = PRM[inp]
        return 0b0010

    elif i == 0b1111: # stp
        return 0b0001

def run_program():
    global ACC
    global CIR
    global OUT
    global PRM
    global PRO
    global PC

    instruction_set(PRO[0],0,0) # check first instruction for start
    for entry in range(len(PRO)):

        if PC == 0b0010: # check if current entry is an input
            PC = 0b0000
            continue

        if PC == 0b0001:
            print(OUT)
            break

        PC = instruction_set(PRO[entry],PRO[entry+1],entry)

    

run_program()

