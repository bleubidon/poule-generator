class TurtleDecoder:
    def __init__(self):
        self.instructions = []

    def instruction(self, instr: str):
        self.instructions.append(instr + '\n')


decoder = TurtleDecoder()


def speed(my_speed):
    pass


def forward(lenght):
    decoder.instruction(f'f:{lenght}')


def backward(length):
    decoder.instruction(f'b:{length}')


def left(angle):
    decoder.instruction(f'l:{angle}')


def right(angle):
    decoder.instruction(f'r:{angle}')


def up():
    decoder.instruction('u')


def down():
    decoder.instruction('d')


def setangle(value=0):
    decoder.instruction(f'a:{value}')


def setpos(pos):
    decoder.instruction(f'se:{pos[0]},{pos[1]}')
