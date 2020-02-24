import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("hey tell me what file to read in")
try:
    with open(sys.argv[0]) as file:
        for line in file:
            split_line = line.split("#")
            maybe_command = split_line[0]
            if len(maybe_command) > 0:
                maybe_command.strip()
                if maybe_command[0] == "1" or maybe_command[0] == "0":
                    print(maybe_command)
except FileNotFoundError:
    print("hey, that file doesn not exist")
