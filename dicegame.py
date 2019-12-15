import random
dicemin = 1
dicemax = 6
total1 = 0
total2 = 0
over_total1 = 0
over_total2 = 0
enter = 0
while enter == 0:
    password = input('Authorization Password: ')
    if password == "321":
        enter += 1
    else:
        print('Incorrect. Try again')
print("Welcome to the dice game!")

player1 =input("Player 1: ")
player2 = input("Player 2: ")
print("")
round = 0

for i in range(5):
    p1r1 = random.randint(dicemin, dicemax)
    p1r2 = random.randint(dicemin, dicemax)
    p2r1 = random.randint(dicemin, dicemax)
    p2r2 = random.randint(dicemin, dicemax)

    total1 += p1r1 + p1r2
    total2 += p2r1 + p2r2
    round += 1
    print(player1 + "'s Roll:", p1r1, "+", p1r2, "=", total1)
    if p1r1 == p1r2:
        double_no1 = random.randint(dicemin, dicemax)
        total1 += double_no1
        print(player1, "got a double so another dice was rolled, +", double_no1)

    if (total1 % 2) == 0:
        total1 += 10
        print("The sum of the outcome was even so 10 was added")
    else:
        total1 += 5
        print("The sum of the outcome was odd so 5 was added")
    over_total1 += total1
    print(player1, "just got", total1, "and their total is",over_total1)
    print()
    print("Enter to roll", player2)
    total1 = 0
    input()

    print(player2 + "'s Roll:", p2r1, "+", p2r2, "=", total2)
    if p2r1 == p2r2:
        double_no2 = random.randint(dicemin, dicemax)
        total2 += double_no2
        print(player2, "got a double so another dice was rolled, +", double_no2)
    if (total2 % 2) == 0:
        total2 += 10
        print("The sum of the outcome was even so 10 was added")
    else:
        total2 += 5
        print("The sum of the outcome was odd so 5 was added")
    over_total2 += total2
    print(player2, "just got", total2, "and their total is", over_total2)
    if round < 5:
        print()
        print("Enter to roll", player1)
        input()
    total2 = 0

while over_total1 == over_total2:
    print("Both players has the same score so you both get to roll again")
    over_total1 += random.randint(dicemin, dicemax)
    over_total2 += random.randint(dicemin, dicemax)
    if over_total1 > over_total2:
        print(player1, "won with", over_total1, "points and", player2, "came second with", over_total2, "points!")
    if over_total1 < over_total2:
        print(player2, "won with", over_total2, "points and", player1, "came second with", over_total1, "points!")
else:
    if over_total1 > over_total2:
        print(player1, "won with", over_total1, "points and", player2, "came second with", over_total2, "points!")
    if over_total1 < over_total2:
        print(player2, "won with", over_total2, "points and", player1, "came second with", over_total1, "points!")

leaderboard = open("leaderboard.txt", "r+")
leaderboard.write(player1 + " - " + '{}'.format(over_total1))
leaderboard.write('\n')
leaderboard.write(player2 + " - " + '{}'.format(over_total2))
leaderboard.close()

print("")
print("Leaderboard:")
players = list()
with open("leaderboard.txt", "r+") as fin:
    for line in fin:
        players.append(line.strip())
        print(line, end="")
players.sort()
