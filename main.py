import sys
import math
file = open(sys.argv[1]).readlines()
sp = -1
#file = open("filer.tn").readlines()
msize = int(file[-1])
mem = [0] * msize
pc = 0
for line in file:
    ln = 0
    pc += 1
    proc = line.split()
    if proc[0] == "print":
        print(mem[sp])
    elif proc[0] == "msp":
        sp = sp + int(proc[1])
    elif proc[0] == "smem":
        mem[sp] = " ".join(proc[1:])
    elif proc[0] == "dmem":
        mem.pop(sp)
    elif proc[0] == "add":
        mem[sp] = int(mem[sp]) + int(mem[sp + int(proc[1])])
    elif proc[0] == "dec":
        mem[sp] = int(mem[sp]) - int(mem[sp + int(proc[1])])
    elif proc[0] == "mul":
        mem[sp] = int(mem[sp]) * int(mem[sp + int(proc[1])])
    elif proc[0] == "div":
        mem[sp] = math.floor(int(mem[sp]) / int(mem[sp + int(proc[1])]))
    elif proc[0] == "in":
        mem[sp] = input()
    elif proc[0] == "loopn":
        ln = int(mem[sp + int(proc[1])]) - 1
        l = 0
        while ln != l:
            l += 1
            for line in file[pc:]:
                proc = line.split()
                if proc[0] == "print":
                    print(mem[sp])
                elif proc[0] == "msp":
                    sp = sp + int(proc[1])
                elif proc[0] == "smem":
                    mem[sp] = " ".join(proc[1:])
                elif proc[0] == "dmem":
                    mem.pop(sp)
                elif proc[0] == "add":
                    mem[sp] = int(mem[sp]) + int(mem[sp + int(proc[1])])
                elif proc[0] == "dec":
                    mem[sp] = int(mem[sp]) - int(mem[sp + int(proc[1])])
                elif proc[0] == "mul":
                    mem[sp] = int(mem[sp]) * int(mem[sp + int(proc[1])])
                elif proc[0] == "div":
                    mem[sp] = math.floor(int(mem[sp]) / int(mem[sp + int(proc[1])]))
                elif proc[0] == "in":
                    mem[sp] = input()
                elif proc[0] == "lend":
                    break
