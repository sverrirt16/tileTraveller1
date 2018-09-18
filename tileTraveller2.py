def calc_tile11(direction):
    while direction != 'N':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 1.2
        else:
            print('Not a valid direction!')

def calc_tile12(direction):
    while direction != 'N' and direction != 'S' and direction != 'E':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 1.3
        elif direction == 'E':
            return 2.2
        elif direction == 'S':
            return 1.1
        else:
            print('Not a valid direction!')
def calc_tile13(direction):
    while direction != 'E' and direction != 'S':
        direction = str(input("Direction: ")).upper()
        if direction == 'E':
            return 2.3
        elif direction == 'S':
            return 1.2
        else:
            print('Not a valid direction!')

def calc_tile21(direction):
    while direction != 'N':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 2.2
        else:
            print('Not a valid direction!')

def calc_tile22(direction):
    while direction != 'W' and direction != 'S':
        direction = str(input("Direction: ")).upper()
        if direction == 'S':
            return 2.1
        elif direction == 'W':
            return 1.2
        else:
            print('Not a valid direction!')
def calc_tile23(direction):
            while direction != 'E' and direction != 'W':
                direction = str(input("Direction: ")).upper()
                if direction == 'E':
                    return 3.3
                elif direction == 'W':
                    return 1.3
                else:
                    print('Not a valid direction!')

def calc_tile32(direction):
    while direction != 'N' and direction != 'S':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 3.3
        elif direction == 'S':
            return 3.1
        else:
            print('Not a valid direction!')

def calc_tile33(direction):
    while direction != 'S' and direction != 'W':
        direction = str(input("Direction: ")).upper()
        if direction == 'S':
            return 3.2
        elif direction == 'W':
            return 2.3
        else:
            print('Not a valid direction!')

current_tile = 1.1
s = 'You can travel: '

while current_tile != 3.1:
    if current_tile == 1.1:
        print(s + '(N)orth.')
        direction = ''
        current_tile = calc_tile11(direction)

    if current_tile == 1.2:
        print(s + '(N)orth or (E)ast or (S)outh.')
        direction = 'W'
        current_tile = calc_tile12(direction)

    if current_tile == 1.3:
        print(s + '(E)ast or (S)outh.')
        direction = ''
        current_tile = calc_tile13(direction)

    if current_tile == 2.1:
        print(s + '(N)orth.')
        direction = ''
        current_tile = calc_tile21(direction)

    if current_tile == 2.2:
        print(s + '(S)outh or (W)est.')
        direction = ''
        current_tile = calc_tile22(direction)

    if current_tile == 2.3:
        print(s + '(E)ast or (W)est.')
        direction = ''
        current_tile = calc_tile23(direction)

    if current_tile == 3.2:
        print(s + '(N)orth or (S)outh.')
        direction = ''
        current_tile = calc_tile32(direction)
    
    if current_tile == 3.3:
        print(s + '(S)outh or (W)est.')
        direction = ''
        current_tile = calc_tile33(direction)

print('Victory!')
