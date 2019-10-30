

PRINT_TIM = 0b01
HALT = 0b10

memory = [
    PRINT_TIM,
    PRINT_TIM,
    PRINT_TIM,
    PRINT_TIM,
    HALT
]

running = True

# PROGRAM COUNTER
pc = 0

while running:
    command = memory[pc]

    if command == PRINT_TIM:
        print("TIM!")

        pc += 1

    elif command == HALT:
        running = False

    else:
        print("I'm confused and scared")
        running = False
