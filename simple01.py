

PRINT_TIM = 0b01
HALT = 0b10
PRINT_NUM = 0b11
SAVE = 0b100
ADD = 0b101
PRINT_REGISTER = 0b110

memory = [
    PRINT_TIM,
    PRINT_NUM,
    0b01,
    PRINT_NUM,
    0b111,
    PRINT_NUM,
    0b1111,
    PRINT_TIM,
    SAVE,
    0b1,
    0b01,
    ADD,
    0b11,
    0b10,
    PRINT_TIM,
    HALT
]

registers = [0] * 8

running = True

# PROGRAM COUNTER
pc = 0

while running:
    command = memory[pc]

    if command == PRINT_TIM:
        print("TIM!")
        pc += 1

    elif command == PRINT_NUM:
        number_to_print = memory[pc + 1]
        print(number_to_print)
        pc += 2

    elif command == HALT:
        running = False

    elif command == ADD:
        first_register_address = memory[pc + 1]
        second_register_address = memory[pc + 2]

        first_num = registers[first_register_address]
        second_num = registers[second_register_address]

        total = first_num + second_num

        registers[first_register_address] = total

        pc += 3

    elif command == SAVE:
        variable = memory[pc + 1]
        register = memory[pc + 2]
        registers[register] = variable
        pc += 3

    else:
        print("I'm confused and scared")
        running = False

print(registers)
