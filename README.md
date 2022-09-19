# 4 bit computer emulation

This project simulates a basic 4 bit computer.

---
The computer has a few instructions being:
```
0x0 - sta - start program

0x1 - add - add the data of an address to ACC

0x2 - sub - subtract the data of an address from ACC

0x3 - mov - move the data of PRM_1 to PRM_2

0x4 - lda - load the data of an address into ACC

0x5 - wrt - write ACC to an address in PRM

0x6 - out - write an address in PRM to OUT

0x7 - jmp - jump to an address on PRO specified by CIR

0x8 - ldc - load the data of an address into CIR

0xF - stp - stop program
```
The computer also has a few registers being:

```
CIR - 4-bit INT
ACC - 4-bit INT used for calculations
OUT - 4 bit INT always printed at the termination of a program
PRM - 16 addresses of 4-bit INTs, general purpose RAM
PRO - 16 addresses of 4-bit INTs, program space (ROM)
```