import sqlite3

ish_spisok = []
conn = sqlite3.connect("players_db.db")
cursor = conn.cursor()
with open("team.txt", encoding='utf-8-sig') as inf:
    for line in inf:
        a = line.strip().split("\t")
        ish_spisok.append(a)

# print(ish_spisok)
# query_add_user = '''
# CREATE TABLE PLAYERS
# (id INTEGER PRIMARY KEY
# , name VARCHAR(30) NOT NULL
# , speed FLOAT
# , stamina FLOAT
# , passing FLOAT
# , shot FLOAT
# , teamplay FLOAT
# , goalkeeping FLOAT
# , amplua VARCHAR (30)
# , average_stats FLOAT)
# '''
# cursor.execute(query_add_user)
# conn.commit()
print(ish_spisok)

conn = sqlite3.connect("players_db.db")
cursor = conn.cursor()
for i in range(1, len(ish_spisok)):
    name = ish_spisok[i][1]
    speed = ish_spisok[i][2]
    stamina = ish_spisok[i][3]
    passing = ish_spisok[i][4]
    shot = ish_spisok[i][5]
    teamplay = ish_spisok[i][6]
    goalkeeping = ish_spisok[i][7]
    amplua = ish_spisok[i][8]
    average_stats = ish_spisok[i][9]

    query_add_users = f'''
        INSERT INTO players
        (name, speed, stamina, passing, shot, teamplay, goalkeeping, amplua, average_stats)
        VALUES (
    "{name}", {speed}, {stamina}, {passing}, {shot}, {teamplay}, {goalkeeping}, "{amplua}", {average_stats})'''

    cursor.execute(query_add_users)
    conn.commit()
