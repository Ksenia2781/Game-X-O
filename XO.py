def game():
    print('Игра "Крестики - нолики"')
game()
cells = [[" "] * 3 for  i in range(3)]

def demo():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {cells[i][0]} {cells[i][1]} {cells[i][2]}")

def motion():
    while True:
        steps = input(" Ваш ход: ").split()

        x, y = steps

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if cells[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def win():
    win_step = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for step in win_step:
        symbols = []
        for c in step:
            symbols.append(cells[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False

count = 0
while True:
    count += 1
    demo()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = motion()

    if count % 2 == 1:
        cells[x][y] = "X"
    else:
        cells[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Ничья!")
        break