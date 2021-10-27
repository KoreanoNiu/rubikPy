import numpy as np
import cube
import movements as move

move._2U()
move.b()
move._2D()
move.b()
move._2R()
move.b()
move._2D()
move.B()
move._2F()
move._2L()
move.D()
move.L()
move.U()
move.f()
move.r()
move.f()
move._2L()
move._2R()
move.U()
move.F()

print('\nYELLOW')
for i in range(3):
    for j in range(3):
        print(cube.yellow[i][j], end='   ')
    print('');

print('\nRED')
for i in range(3): 
    for j in range(3):
        print(cube.red[i][j], end='   ')
    print('');

print('\nWHITE')
for i in range(3): 
    for j in range(3):
        print(cube.white[i][j], end='   ')
    print('');

print('\nORANGE')
for i in range(3): 
    for j in range(3):
        print(cube.orange[i][j], end='   ')
    print('');

print('\nGREEN')
for i in range(3): 
    for j in range(3):
        print(cube.green[i][j], end='   ')
    print('');

print('\nBLUE')
for i in range(3): 
    for j in range(3):
        print(cube.blue[i][j], end='   ')
    print('');

cube._print_()