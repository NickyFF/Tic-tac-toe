desk = list(range(1, 10))

def draw_board(desk):
    print ("-------------")
    for i in range(3):
        print(("|"), desk[0+i*3], "|", desk[1+i*3], "|", desk[2+i*3], "|")
        print("-------------")

def input_value(player_choice):
    while True:
        player_answer = input(f"Выберите блок {player_choice} ? ")
        if player_answer.isdigit():
            player_answer = int(player_answer)
        else:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(desk[player_answer-1]) not in "XO"):
                desk[player_answer-1] = player_choice
                break
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(desk):
    win_cord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_cord:
        if desk[each[0]] == desk[each[1]] == desk[each[2]]:
            return desk[each[0]]
    return False

def main(desk):
    counter = 0
    while True:
        draw_board(desk)
        if counter % 2 == 0:
            input_value("X")
        else:
            input_value("O")
        counter += 1
        if counter > 4:
            p_win = check_win(desk)
            if p_win:
                print(p_win, "выиграл!")
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(desk)

main(desk)