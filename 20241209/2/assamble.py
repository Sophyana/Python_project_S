import math

class AssemblerInterpreter:
    def __init__(self, program):
        self.program = program
        self.variables = {}
        self.labels = {}
        self.commands = []

    def parse_value(self, value):
        try:
            return float(value)
        except ValueError:
            return self.variables.get(value, 0.0)

    def parse_program(self):
        for line_number, line in enumerate(self.program.splitlines()):
            line = line.lstrip()
            if not line:
                continue

            if ":" in line:
                label, _, command = line.partition(":")
                self.labels[label.strip()] = len(self.commands)
                line = command.strip()

            if line:
                self.commands.append((line_number + 1, line.split()))

    def execute(self):
        self.parse_program()
        pointer = 0

        while pointer < len(self.commands):
            line_number, tokens = self.commands[pointer]

            if not tokens:
                pointer += 1
                continue

            cmd = tokens[0]

            if cmd == "stop":
                break

            elif cmd == "store" and len(tokens) == 3:
                _, value, dest = tokens
                self.variables[dest] = self.parse_value(value)

            elif cmd in {"add", "sub", "mul", "div"} and len(tokens) == 4:
                _, src, op, dest = tokens
                src_value = self.parse_value(src)
                op_value = self.parse_value(op)

                if cmd == "add":
                    self.variables[dest] = src_value + op_value
                elif cmd == "sub":
                    self.variables[dest] = src_value - op_value
                elif cmd == "mul":
                    self.variables[dest] = src_value * op_value
                elif cmd == "div":
                    self.variables[dest] = src_value / op_value if op_value != 0 else math.inf

            elif cmd in {"ifeq", "ifne", "ifgt", "ifge", "iflt", "ifle"} and len(tokens) == 4:
                _, src, op, label = tokens
                src_value = self.parse_value(src)
                op_value = self.parse_value(op)

                condition = {
                    "ifeq": src_value == op_value,
                    "ifne": src_value != op_value,
                    "ifgt": src_value > op_value,
                    "ifge": src_value >= op_value,
                    "iflt": src_value < op_value,
                    "ifle": src_value <= op_value,
                }[cmd]

                if condition:
                    if label in self.labels:
                        pointer = self.labels[label]
                        continue
                    else:
                        return

            elif cmd == "out" and len(tokens) == 2:
                _, src = tokens
                print(self.parse_value(src))

            pointer += 1


import sys
program = sys.stdin.read()
interpreter = AssemblerInterpreter(program)
interpreter.execute()

