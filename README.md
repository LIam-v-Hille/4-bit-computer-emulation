# 4 bit computer emulation

This project simulates a basic 4 bit computer.

---
The computer has a few instructions being:
```
0x0 - div - divide ACC by the data of an address - 1 input

0x1 - add - add the data of an address to ACC - 1 input

0x2 - sub - subtract the data of an address from ACC - 1 input

0x3 - mov - move the data of PRM_1 to PRM_2 - 2 input

0x4 - lda - load the data of an address into ACC - 1 input

0x5 - wrt - write ACC to an address in PRM - 1 input

0x6 - out - write an address in PRM to OUT - 1 input

0x7 - jmp - jump to an address on PRO specified by CIR - 0 input

0x8 - ldc - load the data of an address into CIR - 1 input

0x9 - mlt - multiply the ACC by the data of an address - 1 input

0xA - cmp - compare the data of an address with the data of ACC - 1 input

0xB - ift - execute the instruction 2 infront of it if the address 1 infront of it is >=1 - 2 input

0xC - wro - print the OUT register - 0 input

0xD - inp - get user input and write it to the INP register - 0 input

0xE - wrg - write any register (according to the following nibble) to an address in PRM - 2 input

0xF - stp - stop program - 0 input
```
The computer also has a few registers being:

```
PRC - program counter, used by PRO to execute commands
INP - 4-bit INT used for user input
CIR - 4-bit INT
ACC - 4-bit INT used for calculations
OUT - 4 bit INT always printed at the termination of a program
PRM - 16 addresses of 4-bit INTs (addresses can be incresed if you increase the bit count), general purpose RAM
PRO - 16 addresses (can go longer without changing the bit count if you don't want to jump past 15) of 4-bit INTs, program space (ROM)
```