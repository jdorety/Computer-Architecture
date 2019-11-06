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
        try:
            load_file = open(path, 'r')
            address = 0
            for line in load_file:
                split_line = line.split("#")
                possible_command = split_line[0]
                if len(possible_command) > 0:
                    possible_command = possible_command.strip()
                    if possible_command == "":
                        pass
                    else:
                        command = int(possible_command, 2)
                        self.ram[address] = command
                        address += 1
            load_file.close()
        except(FileNotFoundError):
            print("file not found")
        # For now, we've just hardcoded a program:

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
            command = self.ram[ir]
            operands = (command >> 6) + 1

            if command == self.HLT:
                running = False

            elif command == self.LDI:

                reg_add = self.ram[ir + 1]
                value = self.ram[ir + 2]
                self.reg[reg_add] = value

                # self.pc = + 3

            elif command == self.PRN:

                reg_add = self.ram[ir + 1]
                value = self.reg[reg_add]
                print(value)

                # self.pc += 2
            self.pc += operands
            # else:
            # self.pc = self.pc + 1
