import tkinter as tk
from functions import db_list_getter, players_create, team_clbr, team_power, add_user_render
from classes import List_players

ar_cb_val = []


class MainForm(tk.Frame):
    def __init__(self, master=None, service=None):
        super().__init__(master)

        self.grid()
        self.list_players = List_players()
        self.players = db_list_getter()
        self.service = service
        # self.ish_spisok.remove(self.ish_spisok[0])
        self.player_frame = self.render_players()
        self.buttons_frame = self.render_control_buttons()
        # self.active_players_list = self.active_players()

    # отрисовываем список игроков
    def render_players(self):
        list_frame = tk.Frame(self)
        list_frame.grid(sticky="W", row=2, column=0)

        lbl = tk.Label(list_frame, text="Выбирите участников матча:", font="Candara 15")
        lbl.grid(sticky="W", row=2, column=0)
        y = 1
        global ar_cb_val

        for i in range(len(self.players)):
            player_row = tk.Frame(list_frame)
            player_row.grid(sticky="W", row=(2 + y), column=0)

            ar_cb_val.append(tk.BooleanVar())
            btn_check = tk.Checkbutton(player_row, text=self.players[i][1], variable=ar_cb_val[i])
            btn_check.grid(sticky="W", row=(2 + y), column=0)
            y += 1

        return list_frame

    # отрисовываем кнопки
    def render_control_buttons(self):
        buttons_frame = tk.Frame(self)
        buttons_frame.grid(sticky="S", row=26, column=0, columnspan=2)

        btn_create_team = tk.Button(buttons_frame, text="Сформировать команды", command=lambda: self.comm_btn())
        btn_create_team.grid(sticky="S", row=26, column=1, columnspan=2)

        btn_add_player = tk.Button(buttons_frame, text="Добавить игрока", command=lambda: add_user_render())
        btn_add_player.grid(sticky="S", row=27, column=1, columnspan=2)

        btn_delete_player = tk.Button(buttons_frame, text="Удалить игрока")
        btn_delete_player.grid(sticky="S", row=28, column=1, columnspan=2)

        return buttons_frame

    # команды для кнопки "Сформировать команды"
    def comm_btn(self):
        self.check_chb()
        self.active_players()
        team_clbr(self.team_creator()[0], self.team_creator()[1])
        self.team_render()

    # проверка чекбатона и добавление статуса в конец списка
    def check_chb(self):
        for i in range(len(self.players)):
            self.players[i].append(ar_cb_val[i].get())
        # print(self.players)
        return self.players

    # формирование кортежа активных участников
    def active_players(self):
        active_players_list = []
        for player in self.players:
            if player[-1]:
                active_players_list.append(player)

        return active_players_list

    # определям количество игроков в командах
    def div_players_team(self):
        players_yes = players_create(self.active_players())
        team_1_cnt = len(players_yes) // 2
        team_2_cnt = len(players_yes) - team_1_cnt

        return team_1_cnt, team_2_cnt

    # формируем команды
    def team_creator(self):
        say_yes = players_create(self.active_players())
        # global team_1, team_2
        team_1 = []
        team_2 = []

        # формируем команду №1
        for i in range(self.div_players_team()[0]):
            team_1.append(say_yes[i])
        # print(team_1)

        # формируем команду №2
        for i in range(self.div_players_team()[0], self.div_players_team()[0] + self.div_players_team()[1]):
            team_2.append(say_yes[i])
        # print(team_2)
        return team_1, team_2

    # вывод команд в окно
    def team_render(self):
        team1, team2 = team_clbr(self.team_creator()[0], self.team_creator()[1])

        top_window = tk.Toplevel()
        top_window.geometry("400x300")
        top_window.title = "Вывод результата"

        lbl_main = tk.Label(top_window, text="Команды сформированы:", font="Candara 15")
        lbl_main.grid(sticky="W", row=0, column=0)

        lbl_team_1 = tk.Label(top_window, text="Команда №1:", font="Candara 13")
        lbl_team_1.grid(sticky="W", row=1, column=0)
        row = 2
        for player in team1:
            lbl_player = tk.Label(top_window, text=player.name)
            lbl_player.grid(sticky="W", row=row, column=0)
            row += 1

        lbl_team_2 = tk.Label(top_window, text="Команда №2", font="Candara 13")
        lbl_team_2.grid(sticky="W", row=1, column=1)
        row = 2
        for player in team2:
            lbl_player = tk.Label(top_window, text=player.name)
            lbl_player.grid(sticky="W", row=row, column=1)
            row += 1

        team1_power = team_power(team1)
        lbl_team_power_1 = tk.Label(top_window, text=f"Мощь команды №1: " + str(team1_power))
        lbl_team_power_1.grid(sticky="W", row=10, column=0)

        team2_power = team_power(team2)
        lbl_team_power_2 = tk.Label(top_window, text=f"Мощь команды №1: " + str(team2_power))
        lbl_team_power_2.grid(sticky="W", row=10, column=1)
