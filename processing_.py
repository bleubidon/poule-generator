from math import cos, sin, radians as rad, ceil, sqrt
import numpy as np
from typing import List, Tuple
from matplotlib import pyplot as plt
from matplotlib import cm


def instructions_to_positions(instructions: List[str], pos_init: np.ndarray) -> List[Tuple[np.ndarray, bool]]:
    positions = [(pos_init, True)]
    
    pos = pos_init.astype("float64")
    angle = 0
    trace = True

    for instruction in instructions:
        parameter = None
        if ':' in instruction:
            command, parameter = instruction.split(':')
            if ',' in parameter:
                parameter = list(map(float, parameter.split(',')))
            else:
                parameter = float(parameter)
                pass

        else:
            command = instruction

        # handle instruction
        if command == 'f':
            pos += parameter * np.array([-sin(rad(angle)), cos(rad(angle))])
            positions.append((np.array(pos), trace))

        elif command == 'b':
            pos -= parameter * np.array([-sin(rad(angle)), cos(rad(angle))])
            positions.append((np.array(pos), trace))
    
        elif command == 'l':
            angle += parameter
    
        elif command == 'r':
            angle -= parameter

        elif command == 'a':
            angle = parameter

        elif command == 'se':
            pos = np.array(parameter[::-1])
            positions.append((np.array(pos), False))

        elif instruction == 'u':
            trace = False

        elif instruction == 'd':
            trace = True



    return positions

# It seems that this method takes much time to execute
def draw_positions(positions: List[Tuple[np.ndarray, bool]], img_size: Tuple[int, int]) -> np.ndarray:
    void_color = (0, 0, 0, 0)
    my_color = (255, 0, 0)
    special_color = (0, 255, 0)

    # init img
    img = np.zeros(img_size + (4,), dtype=np.uint8)
    img[:, :] = void_color

    pos_prev = np.array(positions[0][0])
    color = 0
    for position, trace in positions:
        if trace:
            diff = position - pos_prev
            # length = np.linalg.norm(diff)
            length = sqrt(diff[0]**2+diff[1]**2)
            if length == 0:
                continue

            n = ceil(length)
            step = diff / n
            for i in range(n + 1):
                point = pos_prev + i * step

                # img[int(point[0]+.5), int(point[1]+.5)] = my_color

                # cmap = cm.ScalarMappable(cmap=plt.get_cmap('nipy_spectral'))
                # color_ = np.array(cmap.to_rgba(color % 1, norm=False)) * 255
                # color += .01

                color_ = (0,255,0,255)
                for _ in range(10):
                    radius = 6
                    img[int(point[0] + .5)+np.random.randint(-radius, radius), int(point[1] + .5)+np.random.randint(-radius, radius)] = color_

        pos_prev = position

    return img.astype("uint8")


def parse_to_img(filename: str, img_size: Tuple[int, int], pos_init: Tuple[float, float]):
    pos_init = np.array(pos_init[::-1])

    # Load instructions
    with open(filename, 'r') as f:
        instructions = f.read().splitlines()

    positions = instructions_to_positions(instructions, pos_init)
    myresult = draw_positions(positions, img_size)

    return myresult
