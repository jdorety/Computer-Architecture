"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [00000000] * 32
        self.reg = [00000000] * 8
        self.pc = 0
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111

    def ram_read(self, mar):
        mdr = self.ram[mar]
        return mdr

    def ram_write(self, mar, mdr):
        value = mdr
        self.ram[mar] = value

    def load(self, path):
        """Load a program into memory."""
        prog_list = []
        load_file = open(path, 'r')
        for line in load_file:
            if line[0] not in ("#", "", "\n"):
                prog_list.append(line)
        load_file.close()

        address = 0
        # For now, we've just hardcoded a program:
        print(prog_list)
        for instruction in prog_list:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running == True:
            ir = self.pc
            if self.ram[ir] == self.HLT:
                running = False

            elif self.ram[ir] == self.LDI:

                reg_add = self.ram[ir + 1]
                value = self.ram[ir + 2]
                self.reg[reg_add] = value

                self.pc = + 3

            elif self.ram[ir] == self.PRN:

                reg_add = self.ram[ir + 1]
                value = self.reg[reg_add]
                print(value)

                self.pc += 2

            else:
                self.pc = self.pc + 1
