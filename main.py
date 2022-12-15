box = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Создаем игровые клетки
win_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# Делим игровые клетки на игровое поле
def paint_box():
    print("-------------")
    for i in range(3):
        print("|", box[0 + i * 3], "|", box[1 + i * 3], "|", box[2 + i * 3], "|")
    print("-------------")

# Создание функцию поставки символа X/0
def put_symbol(token):
    while True:
        value = input("Введите номер клетки на который поставить: " + token + " ?")
        if not (value in "123456789"):    # Проверяем введено ли число из нашего диапазона
            print("Такой клетки нету. Повторите")
            continue
        value = int(value)
        if str(box[value - 1]) in "X0":    # Проверка занята ли клетка или нет
            print("Эта клетка занята. Выберите другую")
            continue
        box[value - 1] = token
        break

# Функция проверки на выигрышную комбинацию
def check_winner():
    for i in win_combination:
        if (box[i[0] - 1]) == (box[i[1] - 1]) == (box[i[2] - 1]):# Условие проверки одинаковые ли 3 символа
            return box[i[0] - 1] # Возвращаем выигрышный символ

def main():  # Основная функция
    count = 0 # Счетчик ходов
    while True: # Определяем какой символ будет поставлен
        paint_box()
        if count % 2 == 0:
            put_symbol("X")
        else:
            put_symbol("0")
        if count > 3: # После 3-х ходов проверяем на победителя
            winner = check_winner()
            if winner:
                paint_box()
                return print(winner + " Выиграл")
                break
        count += 1
        if count > 8: # Больше 8 ходов -> 9 значит ничья
            paint_box()
            print("Ничья!")
            break

main( )




# Половину подсмотрел у людей в интернете и на stackoverflow, да бы более точно разобраться в логике и правильности
# написания функций.