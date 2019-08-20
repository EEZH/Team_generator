from tkinter import *
from tkinter.ttk import Checkbutton

# вводные данные
ish_spisok = [['№п/п', 'ФИО', 'Скорость', 'Выносливость', 'Пас', 'Удар', 'Командность', 'Вратарские навыки', 'Склонность к амплуа', 'Среднее'], ['1', 'Малинкин Павел', '27', '28', '37', '32', '34', '32', 'Защитник', '7,90'], ['2', 'Денис XXX', '28', '24', '29', '37', '27', '3', 'Нападение', '7,25'], ['3', 'Владимир XXX', '34', '31', '32', '32', '34', '3', 'Защитник', '8,15'], ['4', 'Журбенко Евгений', '37', '31', '28', '29', '34', '23', 'Нападение', '7,95'], ['5', 'Хуторянский Кирилл', '35', '31', '32', '35', '23', '3', 'Нападение', '7,80'], ['6', 'Баканов Артур', '32', '31', '33', '34', '34', '3', 'Защитник', '8,20'], ['7', 'Иван Цепляев', '33', '35', '27', '25', '27', '3', 'Нападение', '7,35'], ['8', 'Шеломенцев Михаил', '31', '30', '25', '24', '26', '24', 'Нападение', '6,80'], ['9', 'Заровнятных Дмитрий', '30', '25', '29', '31', '27', '3', 'Нападение', '7,10'], ['10', 'Елфимов Андрей', '24', '23', '24', '28', '26', '22', 'Нападение', '6,25'], ['11', 'Дубинин Алексей', '28', '28', '26', '23', '29', '31', 'Защитник', '6,70'], ['12', 'Саитов Альберт', '27', '29', '25', '23', '24', '6', 'Нападение', '6,40'], ['13', 'Алексакин Александр', '24', '23', '23', '21', '26', '17', 'Нападение', '5,85'], ['14', 'Токарев Алексей', '24', '18', '21', '21', '21', '10', 'Нападение', '5,25'], ['15', 'Дмитрий Мысовских', '31', '24', '28', '29', '25', '20', 'Защитник', '6,85'], ['16', 'Селюнин Дмитрий', '20', '18', '15', '15', '25', '26', 'Вратарь', '4,65'], ['17', 'Хуторянский Ян', '19', '20', '15', '12', '26', '18', 'Защитник', '4,60'], ['18', 'Жуков Евгений', '20', '20', '12', '14', '20', '21', 'Вратарь', '4,30'], ['19', 'Вороновский Александр', '21', '18', '15', '12', '21', '6', 'Защитник', '4,35']]
power_TEAM_Green = 0
power_TEAM_Nacked = 0
delta_TEAM_power = 0
spisok = []
sred = []
TEAM_Green_qnt = int()
komanda_Green = []
komanda_Nacked = []
komanda_Nacked_l = []
komanda_Green_l = []


# выборка тех, кто идёт
def select_player():
    b = []
    for i in range(1, len(ish_spisok)):
        if ish_spisok[i][-1] == True:
            b.append(ish_spisok[i])
    return b

# вывод списка команд в окно
def zap():
    window = Tk()
    window.title("Команды сформированы")
    window.geometry("650x280")

    lblTeamG = Label(window, text="Команда №1:")
    lblTeamG.place(x=0, y=0)
    lblTeamN = Label(window, text="Команда №2:")
    lblTeamN.place(x=300, y=0)
    otstup = 20
    for i in range(len(komanda_Green)):
        lbli = Label(window, text=komanda_Green_l[i])
        lbli.place(x=0, y=0 + otstup)
        otstup += 17
        print(lbli)

    otstup = 20
    for i in range(len(komanda_Nacked)):

        lbli = Label(window, text=komanda_Nacked_l[i])
        lbli.place(x=300, y= 0 + otstup)
        otstup += 17
        print(lbli)

    window.mainloop()

def players_activ():

    window = Tk()
    window.title("Team creator v1.0")
    window.geometry("650x480")

    ar_cb = []
    ar_cbval = []
    for i in range(len(ish_spisok)):
        ar_cbval.append(BooleanVar())
        ar_cb.append(Checkbutton(window, text = ish_spisok[i][1], variable = ar_cbval[i]))
        ar_cb[i].grid(column = 0, row = i,sticky = W)

    # проверка чекбатона и добавление статуса в конец списка
    def mget():
        for i in range(len(ish_spisok)):
            ish_spisok[i].append(ar_cbval[i].get())


        q = {}
        ob_q = {}
        kluchi = []
        spisok_srednih = []
        summa_obshaya = 0
        spisok_k_sort = []
        stats_Team_Green = []
        stats_Team_Nacked = []


        def power_Green():
            power_TEAM_Green = 0
            for i in range(len(stats_Team_Green)):
                power_TEAM_Green = power_TEAM_Green + float(stats_Team_Green[i])  # сила команды Зеленых
            return power_TEAM_Green

        def power_Nacked():
            power_TEAM_Nacked = 0
            for i in range(len(stats_Team_Nacked)):
                power_TEAM_Nacked = power_TEAM_Nacked + float(stats_Team_Nacked[i])  # сила команды Голых
            return power_TEAM_Nacked

        def delta_power():
            delta_TEAM_power = power_Green() - power_Nacked()
            return delta_TEAM_power

        # подгружаем файл и создаем список активных игроков
        # with open("Team.txt", encoding='utf-8-sig') as inf:
        #     for line in inf:
        #         a = line.strip().split("\t")
        #         spisok.append(a)
        # print(spisok)
        # spisok = Test.players_activ
        spisok = select_player()

        # создаем словарь: ФИО - общее значение игрока
        for i in range(len(spisok)):
            q[spisok[i][1]] = [spisok[i][9]]
            # print(q)

        # создаем обратный словарь: общее значение игрока - ФИО
        for i in range(len(spisok)):
            ob_q[spisok[i][9]] = [spisok[i][1]]
            # print(q)

        # выбираем ключи и находим среднее значение
        for value in q.values():
            kluchi.append(value)

        for j in range(len(kluchi)):
            spisok_srednih.append(kluchi[j][0])
        for l in range(len(spisok_srednih)):
            summa_obshaya = summa_obshaya + float(spisok_srednih[l].replace(",", "."))

        # определение кол-ва игроков в командах
        TEAM_Green_qnt = len(spisok_srednih) // 2
        TEAM_Nacked_qnt = len(spisok_srednih) - TEAM_Green_qnt

        # определеяем идеальную силу команд
        ideal_team_power = summa_obshaya / 2
        # print(ideal_team_power)

        # формирование команд
        for l in range(len(spisok_srednih)):
            spisok_k_sort.append(spisok_srednih[l].replace(",", "."))
            spisok_k_sort.sort()  # список от меньшего к большему
        spisok_obratniy = spisok_k_sort[:: -1]  # готовый отсортированный список от большего к меньшему

        # логика выборки Team Green
        for i in range(0, TEAM_Green_qnt - 1, 2):
            stats_Team_Green.append(spisok_obratniy[i])  # топ сильнейших в команде Зеленых

        for j in range(0, TEAM_Green_qnt, 2):
            stats_Team_Green.append(spisok_k_sort[j])
            stats_Team_Green.sort()  # Сформированная команда Зеленых после первой выборки (отсортировано)

        # логика выборки Team Nacked
        spisok_players_copy = spisok_obratniy
        for i in range(len(spisok_players_copy)):
            if spisok_players_copy[i] in stats_Team_Green:
                continue
            else:
                stats_Team_Nacked.append(spisok_players_copy[i])
            stats_Team_Nacked.sort()  # Сформированная команда Голых после первой выборки (отсортировано)

        # Калибровка команд

        while power_Green() - power_Nacked() < -2.5:
            stats_Team_Green.append(stats_Team_Nacked[((len(stats_Team_Nacked) // 2))])
            # stats_Team_Green.sort() #передали игрока из середины списка сильной команды в слабую

            stats_Team_Nacked.remove(stats_Team_Nacked[((len(stats_Team_Nacked) // 2))])  # удалили игрока, которого передали в слабую команду

            stats_Team_Nacked.append(stats_Team_Green[(len(stats_Team_Green) // 2) - 3])
            # stats_Team_Nacked.sort() # передали игрока 2-го по слабости в команду Голых

            stats_Team_Green.remove(stats_Team_Green[(len(stats_Team_Green) // 2) - 3])  # удалили игрока из команды Зеленых
            delta_power()
            # print(stats_Team_Green)
            # print(stats_Team_Nacked)
            # print(power_Green(), power_Nacked())
            # print(delta_power())

        print(stats_Team_Green)
        print(stats_Team_Nacked)
        print(power_Green(), power_Nacked())
        print(delta_power())

        if -1 < delta_power() < 1:
            print("Команды сформированы")

        # выводим ФИО участников команд
        print("Команда Зеленых", TEAM_Green_qnt, "человек:", end="\n ")
        for i in range(len(stats_Team_Green)):
            print(*ob_q[stats_Team_Green[i].replace(".", ",")], end="\n")
            komanda_Green.append(ob_q[stats_Team_Green[i].replace(".", ",")])
            komanda_Green_l.append(komanda_Green[i][0])

        print(*komanda_Green[1])




        print("Команда Голых", TEAM_Nacked_qnt, "человек:", end="\n ")
        for i in range(len(stats_Team_Nacked)):
            print(*ob_q[stats_Team_Nacked[i].replace(".", ",")], end="\n")
            komanda_Nacked.append(ob_q[stats_Team_Nacked[i].replace(".", ",")])
            komanda_Nacked_l.append(komanda_Nacked[i][0])

        print(komanda_Nacked)
        print(komanda_Nacked_l)
        print()





    btn = Button(window, text = "Сформировать команды", command = mget).place(x= 250, y =430)
    btn1 = Button(window, text = "Вывести составы", command = zap). place(x = 250, y = 100)




    window.mainloop()
    # print(ish_spisok)
    # return select_player()
players_activ()



